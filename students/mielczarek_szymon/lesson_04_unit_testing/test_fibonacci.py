import sys
import pytest
sys.path.append('..')
from lesson_03_functions.fibonacci_numbers import fib


class TestFibonacci:
    def test_value_0(self):
        assert fib(0) == 0

    def test_value_1(self):
        assert fib(1) == 1

    def test_value_2(self):
        assert fib(2) == 1

    def test_value_21(self):
        assert fib(21) == 10946

    def test_negative_value(self):
        with pytest.raises(RuntimeError) as exception:
            fib(-1)
        assert 'maximum recursion depth exceeded' in str(exception.value)

    def test_non_integer(self):
        with pytest.raises(TypeError):
            fib('aoeu')

    def test_on_none(self):
        with pytest.raises(TypeError):
            fib(None)
