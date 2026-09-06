def filter_by_state(unsorted_list: list, state: str = "EXECUTED") -> list:
    """Сортировка по указанному ключу: state"""
    list_sort = []
    for x in unsorted_list:
        if x.get("state") == state:
            list_sort.append(x)
        else:
            continue
    return list_sort


def sort_by_date(unsorted_list: list, reverse: bool = True) -> list:
    """Сортировка по дате"""
    return sorted(unsorted_list, key=lambda x: x["date"], reverse=reverse)
