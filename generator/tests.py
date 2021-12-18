"""Tests for project."""

from django.test import TestCase
from generator.models import make_password


class PasswordLengthTestCase(TestCase):
    def test_length_is_zero(self):
        self.assertEqual(make_password(length=0, special=True, numbers=True), "")

    def test_length_is_negative_number(self):
        self.assertEqual(make_password(length=-1, special=True, numbers=True), "")

    def test_length_is_more_than_thousand(self):
        password = make_password(length=1000, special=True, numbers=True)
        self.assertEqual(len(password), 100)

        password = make_password(length=100, special=True, numbers=True)
        self.assertEqual(len(password), 100)

    def test_length_equals_ten(self):
        password = make_password(length=10, special=True, numbers=True)
        self.assertEqual(len(password), 10)
