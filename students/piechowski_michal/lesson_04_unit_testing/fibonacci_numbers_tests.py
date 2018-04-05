#!/usr/bin/env python3

import os
import sys
import unittest
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/lesson_03_functions")

from fibonacci_numbers import fib


class CollatzTest(unittest.TestCase):

    def test_fib_works_with_minimal_input(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

    def test_fib_returns_greater_value_for_greater_input(self):
        self.assertGreater(fib(11), fib(10))

    def test_fib_returns_correct_result(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(25), 75025)
        self.assertEqual(fib(30), 832040)


if __name__ == "__main__":
    unittest.main()
