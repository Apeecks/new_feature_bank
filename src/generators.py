from typing import Any


def filter_by_currency(transactions: list, currency: str) -> Any:
    """Сортировка словаря по ключу currency"""
    if transactions == []:
        raise ValueError("Данные не найдены")

    result = (dict_ for dict_ in transactions if dict_.get("operationAmount").get("currency").get("code") == currency)

    return result


def transaction_descriptions(transactions: list) -> Any:
    """Получение описание транзакции"""
    descriptions = (dict_.get("description") for dict_ in transactions)
    for description in descriptions:
        yield description


def card_number_generator(start: int, stop: int) -> Any:
    """Генерирование номеров карт"""
    for x in range(start, stop):
        result = "0" * (16 - int(len(str(x)))) + str(x)
        result_sort = result[0:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:16]
        yield result_sort
