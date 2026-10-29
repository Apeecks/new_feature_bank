from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(
    no_sort_transactions: list, sort_usd_one_filter_by_currency: list, sort_usd_two_filter_by_currency: list
) -> Any:
    """Тестирование функции filter_by_currency"""
    try:
        usd_transactions = filter_by_currency(no_sort_transactions, "USD")
        assert next(usd_transactions) == sort_usd_one_filter_by_currency
        assert next(usd_transactions) == sort_usd_two_filter_by_currency
    except StopIteration:
        print("Транзакций не найдены")

    with pytest.raises(ValueError) as f:
        filter_by_currency([], "USD")
    assert str(f.value) == "Данные не найдены"


def test_transaction_descriptions(no_sort_transactions: list) -> Any:
    """Тестирование функции transaction_descriptions"""
    try:
        descriptions = transaction_descriptions(no_sort_transactions)
        assert next(descriptions) == "Перевод организации"
        assert next(descriptions) == "Перевод со счета на счет"
        assert next(descriptions) == "Перевод со счета на счет"
    except StopIteration:
        print("Транзакций не найдены")


@pytest.mark.parametrize(
    "start, end, result", [(1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"])]
)
def test_card_number_generator(start: int, end: int, result: Any) -> Any:
    """Тестирование функции card_number_generator"""
    for i, card_number in enumerate(card_number_generator(start, end)):
        assert card_number == result[i]
