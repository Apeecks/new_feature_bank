from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(unsorted_list_state: list, state_canceled: list, state_executed: list) -> None:
    """Проверка функции filter_by_state"""
    assert filter_by_state(unsorted_list_state, "EXECUTED") == state_executed
    assert filter_by_state(unsorted_list_state, "CANCELED") == state_canceled
    assert filter_by_state(unsorted_list_state) == state_executed


def test_sort_by_date(unsorted_list_date: list, sorted_list_date: list, reverse_sorted_list_date: list) -> None:
    """Проверка функции sort_by_date"""
    assert sort_by_date(unsorted_list_date) == sorted_list_date
    assert sort_by_date(unsorted_list_date, False) == reverse_sorted_list_date
