from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_transaction import read_transactions_csv, read_transactions_xlsx
from src.utils import path_to_file_json, process_bank_search
from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная логика работы программы с банковскими транзакциями."""

    print("""
Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

    while True:
        x_file = input("\nВыберите цифру: ")

        if x_file == "1":
            list_dict = path_to_file_json("data/operations.json")
            print("\nДля обработки выбран JSON-файл.")
            break

        elif x_file == "2":
            list_dict = read_transactions_csv("data/transactions.csv")
            print("\nДля обработки выбран CSV-файл.")
            break

        elif x_file == "3":
            list_dict = read_transactions_xlsx("data/transactions_excel.xlsx")
            print("\nДля обработки выбран XLSX-файл.")
            break

        else:
            print("Цифра введена неверно! Выберите цифру из списка.")

    print("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    sort_list = []

    while True:
        x = input("\nВведите статус: ").strip()
        status = x.upper()

        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            sort_list = filter_by_state(list_dict, status)
            print(f'\nОперации отфильтрованы по статусу "{status}"')
            break

        else:
            print(f'Статус операции "{x}" недоступен.')
            print(
                "Введите статус, по которому необходимо выполнить фильтрацию."
                "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )

    while True:
        print("\nОтсортировать операции по дате? Да/Нет")
        x_date = input("\nВведите да/нет: ").strip().lower()

        if x_date not in ["да", "нет", "y", "n"]:
            continue

        elif x_date in ["да", "y"]:
            print("\nОтсортировать по возрастанию(1) или по убыванию(2)?")
            x_revers = input("\nВыберите: 1/2: ").strip().lower()

            if x_revers not in ["1", "2", "по возрастанию", "по убыванию"]:
                continue

            if x_revers in ["1", "по возрастанию"]:
                sort_list = sort_by_date(sort_list, False)
                break
            else:
                sort_list = sort_by_date(sort_list)
                break
        else:
            break

    while True:
        print("\nВыводить только рублевые транзакции? Да/Нет")
        x_rub = input("\nВведите да/нет: ").strip().lower()

        if x_rub not in ["да", "нет", "y", "n"]:
            continue

        if x_rub in ["да", "y"]:
            if x_file in ["2", "3"]:
                sort_list = [x for x in sort_list if x.get("currency_code") == "RUB"]
            else:
                sort_list = list(filter_by_currency(sort_list, "RUB"))
            break
        else:
            break

    while True:
        print("\nОтфильтровать список транзакций по определенному слову в описании?")
        x_search = input("\nВведите да/нет: ").strip().lower()

        if x_search not in ["да", "нет", "y", "n"]:
            continue

        if x_search in ["да", "y"]:
            x_str = input("\nВведите слово поиска: ")
            sort_list = process_bank_search(sort_list, x_str)
            break
        else:
            break

    print("\nРаспечатываю итоговый список транзакций...")

    if not sort_list:
        print("\nНе найдено ни одной транзакции, " "подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(sort_list)}\n")

    for x in sort_list:
        description = x.get("description")
        print(get_date(x.get("date")), description)

        if description == "Открытие вклада":
            print(mask_account_card(x.get("to")))
        else:
            print(f"{mask_account_card(x.get('from'))} -> " f"{mask_account_card(x.get('to'))}")

        if x_file in ["2", "3"]:
            print(f"Сумма: {x.get('amount')} {x.get('currency_code')}\n")
        else:
            print(f"Сумма: {x['operationAmount']['amount']} " f"{x['operationAmount']['currency']['code']}\n")


if __name__ == "__main__":
    main()
