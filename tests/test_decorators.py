import logging
from typing import Any

from src.decorators import log


@log()
def division(a: int, b: int) -> float:
    return a / b


def test_log(caplog: Any) -> None:
    """Проверка логирования успешного выполнения функции."""
    caplog.set_level(logging.INFO)

    result = division(4, 2)

    assert result == 2.0
    assert "Start division" in caplog.text
    assert "division ok" in caplog.text


def test_log_err(caplog: Any) -> None:
    """Проверка логирования ошибки функции."""
    caplog.set_level(logging.INFO)

    division(4, 0)

    assert "division error: ZeroDivisionError" in caplog.text
    assert "Inputs: (4, 0), {}" in caplog.text