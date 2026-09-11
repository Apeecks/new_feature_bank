import os

import requests
from dotenv import load_dotenv


def exchange(operation: dict) -> float:
    """Конвертирует в рубли (API), выводит сумму"""
    amount: float = float(operation["operationAmount"]["amount"])
    from_ = operation["operationAmount"]["currency"]["code"]

    if from_ != "RUB":
        load_dotenv()
        apilayer_key = os.getenv("APILayer_KEY")
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload: dict = {"amount": amount, "to": "RUB", "from": from_}
        headers = {"apikey": apilayer_key}

        response = requests.get(url, headers=headers, params=payload)
        result = response.json()["result"]

        return float(result)

    return float(amount)
