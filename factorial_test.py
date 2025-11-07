# factorial_test.py
# Autor: Jan Hruza

from factorial import *
import unittest

# TestFactorial dedi z unittest.TestCase
class TestFactorial(unittest.TestCase):

    # Pomocna metoda pro testovani faktorialu
    def assert_fact(self, n:int, expected:int) -> None:
        actual = fact(n)
        self.assertEqual(actual, expected)

    # Testovaci metoda pro faktorial
    def test_fact(self) -> None:
        self.assert_fact(0, 1)
        self.assert_fact(1, 1)
        self.assert_fact(2, 2)
        self.assert_fact(5, 120)
        return