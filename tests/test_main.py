from typing import Any

from main import main


def test_main_json(monkeypatch: Any, capsys: Any) -> None:
    """Проверка обработки JSON и поиска по описанию."""
    transactions = [
        {
            "state": "EXECUTED",
            "date": "2019-12-08T00:00:00",
            "description": "Открытие вклада",
            "to": "Счет 1234567890",
            "operationAmount": {
                "amount": "40542",
                "currency": {"code": "RUB"},
            },
        }
    ]

    monkeypatch.setattr(
        "main.path_to_file_json",
        lambda path: transactions,
    )

    monkeypatch.setattr(
        "main.get_date",
        lambda date: "08.12.2019",
    )

    monkeypatch.setattr(
        "main.mask_account_card",
        lambda value: value,
    )

    answers = iter(["1", "executed", "нет", "нет", "да", "вклад"])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers),
    )

    main()

    output = capsys.readouterr().out

    assert "Для обработки выбран JSON-файл" in output
    assert 'Операции отфильтрованы по статусу "EXECUTED"' in output
    assert "Всего банковских операций в выборке: 1" in output
    assert "08.12.2019 Открытие вклада" in output
    assert "Сумма: 40542 RUB" in output


def test_main_empty(monkeypatch: Any, capsys: Any) -> None:
    """Проверка вывода сообщения при пустой выборке."""
    transactions = [
        {
            "state": "EXECUTED",
            "description": "Открытие вклада",
        }
    ]

    monkeypatch.setattr(
        "main.path_to_file_json",
        lambda path: transactions,
    )

    answers = iter(["1", "CANCELED", "нет", "нет", "нет"])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers),
    )

    main()

    output = capsys.readouterr().out

    assert ("Не найдено ни одной транзакции, " "подходящей под ваши условия фильтрации") in output


def test_main_invalid_status(monkeypatch: Any, capsys: Any) -> None:
    """Проверка повторного запроса некорректного статуса."""
    monkeypatch.setattr(
        "main.path_to_file_json",
        lambda path: [],
    )

    answers = iter(["1", "test", "EXECUTED", "нет", "нет", "нет"])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers),
    )

    main()

    output = capsys.readouterr().out

    assert 'Статус операции "test" недоступен.' in output
    assert 'Операции отфильтрованы по статусу "EXECUTED"' in output
