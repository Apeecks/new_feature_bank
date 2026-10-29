from typing import Any
from unittest.mock import mock_open, patch

import pytest

from src.utils import path_to_file_json, search_description, search_str


def test_error_path_to_file(capsys: Any) -> Any:
    """Тестирование обработки ошибок функции"""
    not_found_error = path_to_file_json("")
    out, err = capsys.readouterr()

    assert not_found_error == []
    assert out == "Файл не найден\n"
    assert err == ""

    decode_error = path_to_file_json(".env.example")
    out, err = capsys.readouterr()

    assert decode_error == []
    assert out == "Файл не формата json или пуст\n"
    assert err == ""


@patch("builtins.open", mock_open(read_data='[{"id": 1}]'))
def test_path_to_file() -> None:
    assert path_to_file_json("test.json") == [{"id": 1}]


@patch("builtins.open", mock_open(read_data='{"id": 1}'))
def test_path_to_file_not_list() -> None:
    assert path_to_file_json("test.json") == []


@pytest.mark.parametrize(
    "list_dict, str_search, result",
    [
        ([{"three": "6"}, {"one": "1"}, {"two": "2"}, {"three": "3"}], "three", [{"three": "6"}, {"three": "3"}]),
        ([{"twomath": "10"}, {"two": "3"}, {}], "two", [{"twomath": "10"}, {"two": "3"}]),
        ([{}], "none", []),
        ("two", "none", []),
    ],
)
def test_search_str(list_dict: list, str_search: str, result: dict) -> Any:
    """Проверка функции search_str"""
    assert search_str(list_dict, str_search) == result


def test_search_description(test_utils_list_dict: list) -> Any:
    """Проверка функции search_description"""
    assert search_description(test_utils_list_dict, ["1", "2"]) == {"1": 8, "2": 5}
    assert search_description(test_utils_list_dict, ["1"]) == {"1": 8}
