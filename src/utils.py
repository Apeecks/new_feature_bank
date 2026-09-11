import json
import re
from collections import Counter
from typing import Any


def path_to_file_json(path: str) -> Any:
    """Функция принимающая путь до файла, возвращает список"""
    try:
        try:
            with open(path) as f:
                operation = json.load(f)
                if not isinstance(operation, list):
                    return []
                return operation
        except json.decoder.JSONDecodeError:
            print("Файл не формата json или пуст")
            return []
    except FileNotFoundError:
        print("Файл не найден")
        return []


def search_str(list_dict: list, search_string: str) -> list:
    """Функция поиска в списке словарей по заданной информации"""
    result = []
    for dict_ in list_dict:
        dict_check = re.search(search_string, str(dict_), flags=re.IGNORECASE)
        if dict_check is not None:
            result.append(dict_)
    return result


def search_description(list_dict: list, user_list_description: list) -> dict:
    """Возвращает кол-во всех описаний операций"""
    list_description = []
    result = {}
    for x in list_dict:
        list_description.append(x.get("description"))
    caunter = Counter(list_description)
    for caunt in caunter:
        if caunt in user_list_description:
            result[caunt] = caunter.get(caunt)
    return result
