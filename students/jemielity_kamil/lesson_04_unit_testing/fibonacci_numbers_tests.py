import pytest
from students.jemielity_kamil.lesson_03_functions.fibonacci_numbers \
    import fib


class TestClass(object):

    def test_string_value(self):
        with pytest.raises(ValueError):
            fib('aoeu')

    def test_none_value(self):
        with pytest.raises(TypeError):
            fib(None)

    def test_negative_value(self):
        with pytest.raises(ValueError):
            print(fib(-2))

    def test_power_function_normal_values(self):
        assert fib(3) == 2

    def test_n_equal_to_zero(self):
        assert fib(0) == 0

    def test_float_values(self):
        with pytest.raises(ValueError):
            fib(2.7)
