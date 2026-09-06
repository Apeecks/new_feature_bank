def get_mask_card_number(cart_namber: str) -> str:
    """Маскировка номера банковской карты"""
    return cart_namber[0:4] + " " + cart_namber[4:6] + "**" + " " + "****" + " " + cart_namber[12:16]


def get_mask_account(account: str) -> str:
    """Маскировка номера банковского счета"""
    return account.replace(account[:16], "**")
