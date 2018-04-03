# Tests for Fibonacci
import unittest
import Fibonacci


class FibonacciTest(unittest.TestCase):

    # tests for input
    def test_checkInput_string(self):
        self.assertRaises(TypeError, Fibonacci.fib('aoeu'))
    def test_checkInput_None1(self):
        self.assertRaises(TypeError, Fibonacci.fib(None))
    def test_checkInput_None2(self):
        self.assertIsNotNone(TypeError, Fibonacci.fib(None))
    def test_checkInput_float(self):
        self.assertRaises(TypeError, Fibonacci.fib(25.2))
    def test_checkInput_negative(self):
        self.assertRaises(TypeError, Fibonacci.fib(-2))

    # tests for values
    def test_values_0(self):
        self.assertEqual(Fibonacci.fib(0), 0)
    def test_values_1(self):
        self.assertEqual(Fibonacci.fib(1), 1)
    def test_values_6(self):
        self.assertFalse(Fibonacci.fib(6) == 5)
    def test_values_19(self):
        self.assertEqual(Fibonacci.fib(19), 4181)
    def test_many_values(self):
        l = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i in range(2, 10):
            self.assertTrue(Fibonacci.fib(i) == l[i])

if __name__ == '__main__':
    unittest.main()
