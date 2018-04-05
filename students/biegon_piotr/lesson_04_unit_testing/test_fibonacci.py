import unittest
import pytest
from fibonacci import fib


class TestFibonacciFunction(unittest.TestCase):

    def test_TypeError_when_input_is_None(self):
        with pytest.raises(TypeError):
            fib(None)

    def test_TypeError_when_input_is_string(self):
        with pytest.raises(TypeError):
            fib('asdf')

    def test_RecursionError_when_input_is_zero(self):
        with pytest.raises(RecursionError):
            fib(0)

    def test_RecursionError_when_input_is_negative(self):
        with pytest.raises(RecursionError):
            fib(-5)

    def test_input_1_return_1(self):
        self.assertEqual(1, fib(1))

    def test_input_2_return_1(self):
        self.assertEqual(1, fib(1))

    def test_input_17_output_1597(self):
        self.assertEqual(10946, fib(21))
