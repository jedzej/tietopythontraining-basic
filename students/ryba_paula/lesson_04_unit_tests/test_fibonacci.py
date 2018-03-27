import unittest
from fibonacci_numbers import fib


class TestFibonacci(unittest.TestCase):
    def test_argument_zero(self):
        self.assertEqual(fib(0), 0)

    def test_argument_one(self):
        self.assertEqual(fib(1), 1)

    def test_argument_twenty(self):
        self.assertEqual(fib(20), 10946)

    def test_type_error_string(self):
        self.assertRaises(TypeError, fib, 'a')

    def test_type_error_none(self):
        self.assertRaises(TypeError, fib, None)

    def test_recursion_error_thousand(self):
        self.assertRaises(RecursionError, fib, 1000)


if __name__ == '__main__':
    unittest.main()
