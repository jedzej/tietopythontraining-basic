import unittest
import Fibonacci


class TestFibonacciFunction(unittest.TestCase):
    def test_type_error_when_string_entered(self):
        with self.assertRaises(TypeError):
            Fibonacci.fib("shit")

    def test_type_error_when_none_entered(self):
        with self.assertRaises(TypeError):
            Fibonacci.fib(None)

    def test_negative_integer(self):
        self.assertEqual(Fibonacci.fib(-1), 1)

    def test_zero_entered(self):
        self.assertEqual(Fibonacci.fib(0), 0)

    def test_one_entered(self):
        self.assertEqual(Fibonacci.fib(1), 1)

    def test_expected_fibonacci_nr(self):
        self.assertEqual(Fibonacci.fib(11), 89)
        self.assertEqual(Fibonacci.fib(20), 6765)


if __name__ == '__main__':
    unittest.main()
