import random


def make_password(length, uppercase=False, special=False, numbers=False):
    """Return new password.

    Args:
        length(int): length of the new password
        uppercase(bool): flag of uppercase characters in the new password
        special(bool): flag of special characters in the new password
        numbers(bool): flag of numbers characters in the new password
    Returns:
        password(str): new password
    """
    if length <= 0:
        return ""
    if length > 100:
        length = 100
    symbols = list("qwertyuiopasdfghjklzxcvbnm")
    if uppercase is True:
        symbols.extend([symbol.upper() for symbol in symbols])
    if special is True:
        symbols.extend(list("!@#$%^&*()_+="))
    if numbers is True:
        symbols.extend(list("123456789"))
    return _make(symbols, length, random.choice)


def _make(symbols, length, custom_random):
    """Return new password.

    Args:
        symbols(list): symbols for new password
        length(int): length new password
        custom_random(function): function for choice symbol in symbols
    Returns:
        password(str): new password
    """
    password = ""
    for _ in range(length):
        password += custom_random(symbols)
    return password
