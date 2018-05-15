#!/usr/bin/env python3
"""Coma code exercise"""
import unittest
from .comma_code import comma_code


class Test(unittest.TestCase):
    """Unit test for comma_code function"""

    def test_empty(self):
        """Pass empty list as parameter"""
        self.assertEqual(comma_code([]), '')

    def test_example(self):
        """Pass exercise description list as parameter"""
        self.assertEqual(comma_code(['apples', 'bananas', 'tofu', 'cats']),
                         'apples, bananas, tofu, and cats')

    def test_one_element(self):
        """Pass one element list as parameter"""
        self.assertEqual(comma_code(['apples']), 'apples, ')

    def test_two_element(self):
        """Pass two element list as parameter"""
        self.assertEqual(comma_code(['apples', 'bananas']),
                         'apples, and bananas')

    def test_long_list(self):
        """Pass long list (10 elements) as parameter"""
        in_param = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                    'eight', 'nine', 'ten']
        result = 'one, two, three, four, five, six, seven, eight, nine, ' \
                 'and ten'
        self.assertEqual(comma_code(in_param), result)


if __name__ == '__main__':
    unittest.main()
