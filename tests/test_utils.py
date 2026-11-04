from typing import Any
from unittest.mock import mock_open, patch

import pytest

from src.utils import path_to_file_json, process_bank_operations, process_bank_search


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
        (
            [
                {"description": "Перевод организации"},
                {"description": "Открытие вклада"},
                {"description": "Перевод с карты на карту"},
            ],
            "Перевод",
            [
                {"description": "Перевод организации"},
                {"description": "Перевод с карты на карту"},
            ],
        ),
        (
            [
                {"description": "Открытие вклада"},
                {"description": "Перевод организации"},
            ],
            "вклад",
            [{"description": "Открытие вклада"}],
        ),
        (
            [
                {"description": "Перевод организации"},
            ],
            "перевод",
            [{"description": "Перевод организации"}],
        ),
        (
            [
                {"description": "Открытие вклада"},
            ],
            "Кредит",
            [],
        ),
        (
            [
                {"state": "EXECUTED"},
                {"description": "Открытие вклада", "state": "CANCELED"},
            ],
            "EXECUTED",
            [],
        ),
        (
            [],
            "Перевод",
            [],
        ),
    ],
)
def test_process_bank_search(list_dict: list, str_search: str, result: list) -> None:
    """Проверка поиска транзакций по описанию."""
    assert process_bank_search(list_dict, str_search) == result


def test_process_bank_operations(test_utils_list_dict: list) -> None:
    """Проверка подсчета количества операций по категориям."""
    assert process_bank_operations(test_utils_list_dict, ["1", "2"]) == {"1": 8, "2": 5}

    assert process_bank_operations(test_utils_list_dict, ["1"]) == {"1": 8}
