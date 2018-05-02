import pytest
from fibonacci_rec import fib
# from lesson_03_functions.fibonacci_rec import fib


class TestFibonacciFunction(object):
    def test_none_as_input_parameter(self):
        with pytest.raises(TypeError):
            fib(None)

    def test_string_as_input_parameter(self):
        with pytest.raises(TypeError):
            fib('aoeu')

    def test_real_number_as_input_parameter(self):
        with pytest.raises(TypeError):
            fib('1.3')

    def test_negative_input_exception(self):
        with pytest.raises(ValueError):
            fib(-1)

    def test_zero_as_input_parameter(self):
        assert fib(0) == 0

    def test_one_as_input_parameter(self):
        assert fib(1) == 1

    def test_eight_as_input_parameter(self):
        assert fib(8) == 21
