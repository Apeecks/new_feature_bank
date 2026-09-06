import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, result",
    [
        ("1111111111111111", "1111 11** **** 1111"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(card_number: str, result: str) -> None:
    """Проверка функции get_mask_card_number"""
    assert get_mask_card_number(card_number) == result


@pytest.mark.parametrize(
    "account, result",
    [
        ("11111111111111111111", "**1111"),
        ("11112222333344445555", "**5555"),
        ("12345678901234567890", "**7890"),
    ],
)
def test_get_mask_account(account: str, result: str) -> None:
    """Проверка функции get_mask_account"""
    assert get_mask_account(account) == result
