import unittest
import pytest
from fibonacci_numbers import fib


class TestFibonacciNumbersFunction(unittest.TestCase):

    def test_input_is_None(self):
        with pytest.raises(TypeError):
            fib(None)

    def test_input_is_string(self):
        with pytest.raises(TypeError):
            fib('ajdj')

    def test_input_1_output_1(self):
        self.assertEqual(1, fib(1))

    def test_input_5_output_5(self):
        self.assertEqual(5, fib(5))

    def test_input_17_output_1597(self):
        self.assertEqual(1597, fib(17))
