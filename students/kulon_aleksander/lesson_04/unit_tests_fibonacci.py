from fibonacci_numbers import fib
import pytest
import unittest


class TestFibFunction(unittest.TestCase):

    def test_input_none(self):
        with pytest.raises(TypeError):
            fib(None)

    def test_input_string(self):
        with pytest.raises(TypeError):
            fib('aoeu')

    def test_typical(self):
        self.assertEqual(fib(8), 21, "typical input")

    def test_negative(self):
        with pytest.raises(RecursionError):
            fib(-2)

    def test_zero(self):
        self.assertEqual(fib(0), 0, "0 input")


if __name__ == '__main__':
    unittest.main()
