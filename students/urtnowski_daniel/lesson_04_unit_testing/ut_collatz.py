#!/usr/bin/env python3

"""
ut_collatz.py: Unit tests for collatz() function
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"

import unittest
import sys
from collatz import collatz


class TestCollatz(unittest.TestCase):

    def test_type_error(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_return_value_for_8(self):
        self.assertEqual(collatz(8), 4)

    def test_return_value_for_5(self):
        self.assertEqual(collatz(5), 16)

    def test_value_error(self):
        negative_values = (-1, -2, -sys.maxsize - 1, -123456)
        for value in negative_values:
            self.assertRaises(ValueError, collatz, value)


if __name__ == '__main__':
    unittest.main()

