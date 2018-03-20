#!/usr/bin/env python3

"""
ut_fibonacci.py: Unit tests for fib() function from snakify_lesson8 module
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"

import unittest
import sys
from snakify_lesson8 import fib


class TestFibonacci(unittest.TestCase):

    def test_incorrect_input_type(self):
        self.assertRaises(TypeError, fib, 'aoeu')
        self.assertRaises(TypeError, fib, None)

    def test_negative_input_value(self):
        negative_values = (-1, -2, -sys.maxsize - 1, -123456)
        for value in negative_values:
            self.assertRaises(ValueError, fib, value)

    def test_special_input_values(self):
        params_and_expected_results = ((0, 0), (1, 1), (2, 1))
        for param, expected_result in params_and_expected_results:
            self.assertEqual(fib(param), expected_result,
                             "fib({}) != {}".format(param, expected_result))

    def test_typical_input_values(self):
        params_and_expected_results = ((3, 2), (4, 3), (10, 55), (17, 1597))
        for param, expected_result in params_and_expected_results:
            self.assertEqual(fib(param), expected_result,
                             "fib({}) != {}".format(param, expected_result))


if __name__ == '__main__':
    unittest.main()

