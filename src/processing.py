def filter_by_state(unsorted_list: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список банковских операций по статусу.

    Функция принимает список словарей с банковскими операциями
    и возвращает новый список, содержащий только те операции,
    у которых значение ключа "state" соответствует переданному
    значению.
    Если аргумент state не передан, используется значение
    "EXECUTED".

    Пример:
        operations = [
             {"id": 1, "state": "EXECUTED"},
             {"id": 2, "state": "CANCELED"},
        ]

        filter_by_state(operations, "EXECUTED")
        [{'id': 1, 'state': 'EXECUTED'}]
    """
    list_sort = []
    for x in unsorted_list:
        if x.get("state") == state:
            list_sort.append(x)
        else:
            continue
    return list_sort


def sort_by_date(unsorted_list: list, reverse: bool = True) -> list:
    """
    Сортирует список банковских операций по дате.

    Функция принимает список словарей с банковскими операциями
    и возвращает новый список, отсортированный по значению
    ключа "date".

    По умолчанию сортировка выполняется по убыванию,
    то есть сначала идут более поздние операции.

    Пример:
        operations = [
             {"id": 1, "date": "2018-06-30T02:08:58.425572"},
             {"id": 2, "date": "2019-07-03T18:35:29.512364"},
        ]

        sort_by_date(operations)
        [{'id': 2, 'date': '2019-07-03T18:35:29.512364'}, {'id': 1, 'date': '2018-06-30T02:08:58.425572'}]
    """
    return sorted(unsorted_list, key=lambda x: x["date"], reverse=reverse)
