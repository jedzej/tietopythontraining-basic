#!/usr/bin/env python3

import unittest
from students.piechowski_michal.lesson_03_functions.fibonacci_numbers import fib


class FibonacciTest(unittest.TestCase):

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

    def test_fib_returns_error_on_invalid_type(self):
        self.assertRaises(TypeError, fib, 'X')

    def test_fib_will_not_jump_into_infinite_recursion(self):
        self.assertEqual(fib(-1), -1)
        self.assertEqual(fib(-7), -7)


if __name__ == "__main__":
    unittest.main()
