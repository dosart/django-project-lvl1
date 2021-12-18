"""Tests for project."""

from django.test import TestCase
from generator.models import make
from random import choice


class PasswordLengthTestCase(TestCase):
    def test_length_is_zero(self):
        symbols = ["A", "B"]
        length = 0
        self.assertEqual(make(symbols, length, choice), "")

    def test_length_is_negative_number(self):
        symbols = ["A", "B"]
        length = -1
        self.assertEqual(make(symbols, length, choice), "")

    def test_length_is_more_than_thousand(self):
        symbols = ["A", "B"]
        length = 1000
        password = make(symbols, length, choice)
        self.assertEqual(len(password), 100)

        length = 10000
        password = make(symbols, length, choice)
        self.assertEqual(len(password), 100)


class PasswordSymbolsTestCase(TestCase):
    def test_symbols_for_password_is_empty(self):
        symbols = []
        length = 10

        self.assertEqual(make(symbols, length, choice), "")

    def test_symbols_and_length_is_empty(self):
        symbols = []
        length = 0

        self.assertEqual(make(symbols, length, choice), "")
