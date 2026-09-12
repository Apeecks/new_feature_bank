import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(cart_namber: str) -> str:
    """
    Маскирует номер банковской карты.

    Функция принимает номер банковской карты и возвращает его
    в замаскированном виде. Первые 6 цифр и последние 4 цифры
    остаются видимыми, остальные цифры заменяются символами "*".

    Пример:
        get_mask_card_number("7000792289606361")
        '7000 79** **** 6361'
    """
    if cart_namber == "":
        logger.error("Неправильно введен номер карты")
        raise TypeError("Номер карты не введен")
    elif len(cart_namber) != 16:
        logger.error("Неправильно введен номер карты")
        raise TypeError("Неправильно введен номер карты")
    logger.info("Маскировка карты")
    return cart_namber[0:4] + " " + cart_namber[4:6] + "**" + " " + "****" + " " + cart_namber[12:16]


def get_mask_account(account: str) -> str:
    """
    Маскирует номер банковского счета.

    Функция принимает номер банковского счета и возвращает его
    в замаскированном виде. В результате отображаются только
    последние 4 цифры счета, перед которыми находятся две звездочки.

    Пример:
        get_mask_account("73654108430135874305")
        '**4305'
    """
    if account == "":
        logger.error("Неправильно введен номер счета")
        raise TypeError("Номер счета не введен")
    elif len(account) != 20:
        logger.error("Неправильно введен номер счета")
        raise TypeError("Неправильно введен номер счета")
    logger.info("Маскировка счета")
    return account.replace(account[:16], "**")
