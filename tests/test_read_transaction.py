from unittest.mock import MagicMock, mock_open, patch

from src.read_transaction import read_transactions_csv, read_transactions_xlsx


@patch("builtins.open", mock_open(read_data="id;state;amount\n1;EXECUTED;100\n2;CANCELED;200\n"))
def test_read_transactions_csv() -> None:
    result = read_transactions_csv("test.csv")

    assert result == [
        {"id": "1", "state": "EXECUTED", "amount": "100"},
        {"id": "2", "state": "CANCELED", "amount": "200"},
    ]


@patch("src.read_transaction.pd.read_excel")
def test_read_transactions_xlsx(mock_read_excel: MagicMock) -> None:
    mock_df = MagicMock()

    mock_df.to_dict.return_value = [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "CANCELED", "amount": 200},
    ]

    mock_read_excel.return_value = mock_df

    result = read_transactions_xlsx("test.xlsx")

    assert result == [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "CANCELED", "amount": 200},
    ]

    mock_read_excel.assert_called_once_with("test.xlsx")
    mock_df.to_dict.assert_called_once_with(orient="records")
