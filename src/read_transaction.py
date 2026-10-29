import csv
from typing import Any

import pandas as pd


def read_transactions_csv(path_file_csv: str) -> list:
    """Возвращение списка словарей из файла csv"""
    try:
        with open(path_file_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            list_dict = []
            for row in reader:
                list_dict.append(row)
            return list_dict
    except FileNotFoundError:
        print("Файл не найден")
        return []


def read_transactions_xlsx(path_to_file_exel: str) -> Any:
    """Возвращение списка словарей из файла exel"""
    try:
        df = pd.read_excel(path_to_file_exel)
        df_dict = df.to_dict(orient="records")
        return df_dict
    except FileNotFoundError:
        print("Файл не найден")
        return []
