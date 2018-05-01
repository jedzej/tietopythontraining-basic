from lesson_03.fibonacci_numbers import fib
import pytest


class TestFibFunction(object):

    def test_input_none(self):
        with pytest.raises(TypeError):
            fib(None)

    def test_input_string(self):
        with pytest.raises(TypeError):
            fib('aoeu')

    def test_typical(self):
        assert fib(8) == 21

    def test_negative(self):
        with pytest.raises(RecursionError):
            fib(-2)

    def test_zero(self):
        assert fib(0) == 0
