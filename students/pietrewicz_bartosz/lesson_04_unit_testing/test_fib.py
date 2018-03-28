from fibonacci_numbers import fib
import pytest


class TestFibFunction(object):
    def test_none_parameter(self):
        with pytest.raises(TypeError):
            fib(None)

    def test_string_parameter(self):
        with pytest.raises(TypeError):
            fib('alamakota')

    def test_real_parameter(self):
        with pytest.raises(TypeError):
            fib(4.6)

    def test_negative_parameter(self):
        assert fib(-5) is None

    def test_parameter_value_0(self):
        assert fib(0) == 0

    def test_parameter_value_1(self):
        assert fib(1) == 1

    def test_parameter_value_2(self):
        assert fib(2) == 1

    def test_parameter_value_3(self):
        assert fib(3) == 2

    def test_parameter_value_10(self):
        assert fib(10) == 55

    def test_parameter_value_30(self):
        assert fib(30) == 832040
