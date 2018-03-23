# Test your code from Fibonacci numbers from previous lesson.
# You can use pytest or unittest.
from fibonacci_numbers import fib
import unittest


class FibonacciTest(unittest.TestCase):

    def test_value_error_raised_when_string_is_on_input(self):
        with self.assertRaises(ValueError):
            fib('string')

    def test_returns_21_when_called_on_8(self):
        self.assertEqual(fib(8), 21)

    def test_returns_5_when_called_on_5float(self):
        self.assertEqual(fib(5.5), 5)

    def test_returns_1_when_called_on_1(self):
        self.assertEqual(fib(1), 1)

    def test_returns_1_when_called_on_2(self):
        self.assertEqual(fib(2), 1)
        
    def test_value_error_raised_when_called_on_0(self):
        with self.assertRaises(ValueError):
            fib(0)

    def test_value_error_raised_when_called_on_negative_value(self):
        with self.assertRaises(ValueError):
            fib(-1)

if __name__ == "__main__":
    unittest.main()
