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
    assert "Начало работы функции division" in caplog.text
    assert "Завершение функции division, с результатом 2.0" in caplog.text


def test_log_err(caplog: Any) -> None:
    """Проверка логирования ошибки функции."""
    caplog.set_level(logging.INFO)

    division(4, 0)

    assert "Функция division закончила работу с ошибкой" in caplog.text
    assert "division by zero" in caplog.text
    assert "Args: (4, 0)" in caplog.text
    assert "kwargs: {}" in caplog.text
