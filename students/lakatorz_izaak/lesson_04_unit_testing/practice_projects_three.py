# Test your code from Fibonacci numbers from previous lesson. You can use
# pytest or unittest.

import fibonacci_numbers
import pytest


def test_if_raises_type_error_for_none():
    with pytest.raises(TypeError):
        fibonacci_numbers.fib(None)


def test_if_raises_recursion_error_for_negative():
    with pytest.raises(ValueError):
        fibonacci_numbers.fib(-1)


def test_if_returns_correct_value():
    assert fibonacci_numbers.fib(7) == 13
    assert fibonacci_numbers.fib(17) == 1597
    assert fibonacci_numbers.fib(30) == 832040
