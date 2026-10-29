from typing import Any
from unittest.mock import patch

from src.external_api import exchange


@patch("src.external_api.requests.get")
def test_exchange(mock_get: Any) -> None:
    transaction = {
        "id": 41428829,
        "operationAmount": {
            "amount": "8000",
            "currency": {
                "name": "USD",
                "code": "USD",
            },
        },
    }

    mock_get.return_value.json.return_value = {
        "result": 640000,
    }

    assert exchange(transaction) == 640000.0
