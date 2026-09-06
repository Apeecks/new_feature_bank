from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_cart: str) -> str:
    """
    Маскирует номер банковской карты или банковского счета.

    Функция принимает строку, содержащую название карты или счета
    и его номер. В зависимости от длины номера определяется тип
    данных и применяется соответствующая функция маскировки.

    Для банковской карты используется маска с отображением первых
    6 и последних 4 цифр. Для банковского счета отображаются только
    последние 4 цифры.

    Пример:
        mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'

        mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    number = ""
    for symbol in info_cart:
        if symbol.isdigit():
            number = number + symbol
    if len(number) == 16:
        numser_masks = get_mask_card_number(number)
        info_cart_masks = info_cart.replace(info_cart[-16:], numser_masks)
    else:
        numser_masks = get_mask_account(number)
        info_cart_masks = info_cart.replace(info_cart[-20:], numser_masks)
    return info_cart_masks


def get_date(data: str) -> str:
    """
    Преобразует дату в формат ДД.ММ.ГГГГ.

    Функция принимает строку с датой и временем и возвращает
    только дату в формате день.месяц.год.

    Пример:
        get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    data_t = [data[8:10], data[5:7], data[0:4]]
    return ".".join(data_t)
