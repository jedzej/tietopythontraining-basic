# Test your code from Fibonacci numbers from previous lesson. You can use
# pytest or unittest.

from fibonacci_numbers import fib
import pytest


def test_if_raises_type_error_for_none():
    with pytest.raises(TypeError):
        fib(None)


def test_if_raises_recursion_error_for_negative():
    with pytest.raises(RecursionError):
        fib(-1)


def test_if_returns_correct_value():
        assert fib(7) == 13
        assert fib(17) == 1597
        assert fib(30) == 832040
