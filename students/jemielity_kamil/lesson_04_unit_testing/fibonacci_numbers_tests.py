import pytest
from students.jemielity_kamil.lesson_03_functions.fibonacci_numbers import power


class TestClass(object):

    def test_string_value(self):
        with pytest.raises(TypeError):
            power('aoeu', 'aoeu')

    def test_none_value(self):
        with pytest.raises(TypeError):
            power(None, None)

    def test_negative_power(self):
        with pytest.raises(RecursionError):
            print(power(2, -1))

    def test_power_function_normal_values(self):
        assert power(2, 3) == 8

    def test_n_equal_to_zero(self):
        assert power(2, 0) == 1

    def test_negative_a_value(self):
        assert power(-2, 3) == -8

    def test_float_values(self):
        with pytest.raises(RecursionError):
            power(2.7, 3.5)
