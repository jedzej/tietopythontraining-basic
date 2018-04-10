import pytest
from lesson_04.src.fibonacci_numbers import fib


def test_if_fib_raises_type_error_when_none_provided():
    with pytest.raises(TypeError):
        fib(None)


def test_if_fib_raises_type_error_when_string_provided():
    with pytest.raises(TypeError):
        fib("3")


def test_if_fib_returns_1_when_1_provided():
    assert fib(1) == 1


def test_if_fib_returns_1_when_2_provided():
    assert fib(2) == 1


def test_fib():
    assert fib(6) == 8
    assert fib(10) == 55
