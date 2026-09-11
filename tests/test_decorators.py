from typing import Any

from src.decorators import log


@log()
def division(a: int, b: int) -> float:
    return a / b


@log("log_test.txt")
def add(a: int, b: int) -> float:
    return a + b


def test_log(capsys: Any) -> Any:
    division(4, 2)
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""


def test_log_err(capsys: Any) -> Any:
    division(4, 0)
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
