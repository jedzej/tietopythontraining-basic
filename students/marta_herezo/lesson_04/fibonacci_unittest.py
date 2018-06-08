# Given a non-negative integer n,//
# print the nth Fibonacci number.
import unittest
from fibonacci_numbers import fib


class TestFib(unittest.TestCase):

    def test_0(self):
        self.assertEqual(fib(0), 0, "fib(n) != 0")

    def test_1(self):
        self.assertEqual(fib(1), 1, "fib(n) != 1")

    def test_6(self):
        self.assertEqual(fib(6), 8, "fib(n) != 8")

    def test_val(self):
        with self.assertRaises(ValueError):
            fib(-8)
            print('Enter data is wrong. Please enter only data >= 0')

    def test_typ(self):
        with self.assertRaises(TypeError):
            fib('aoeu')
            print('Enter data is wrong. Please enter only numbers.')


if __name__ == "__main__":
    unittest.main()
