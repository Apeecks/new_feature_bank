import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info_cart, result",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 11111111111111111111", "Счет **1111"),
        ("Счет 11112222333344445555", "Счет **5555"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Classic 1111111111111111", "Visa Classic 1111 11** **** 1111"),
        ("Visa 1111222233334444", "Visa 1111 22** **** 4444"),
    ],
)
def test_mask_account_card(info_cart: str, result: str) -> None:
    """Проверка функции mask_account_card"""
    assert mask_account_card(info_cart) == result


@pytest.mark.parametrize(
    "data, result", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2025-11-10T02:26:18.671407", "10.11.2025")]
)
def test_get_date(data: str, result: str) -> None:
    """Проверка функции get_date"""
    assert get_date(data) == result
