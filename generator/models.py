# -*- coding:utf-8 -*-

"""Implementation of algorithm generate password."""

import secrets
import string


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

    symbols = list(string.ascii_lowercase)
    if uppercase is True:
        symbols.extend(list(string.ascii_uppercase))
    if special is True:
        symbols.extend(list("!@#$%^&*()_+-"))
    if numbers is True:
        symbols.extend(list(string.digits))
    return "".join(secrets.choice(symbols) for _ in range(length))
