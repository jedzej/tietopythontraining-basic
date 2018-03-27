from fibonacci_numbers import fibonacci
import pytest


def test_none_input_exception():
    with pytest.raises(TypeError):
        fibonacci(None)


def test_aoeu_input_exception():
    with pytest.raises(TypeError):
        fibonacci('aoeu')


def test_zero_input():
    assert fibonacci(0) == 0


def test_one_input():
    assert fibonacci(1) == 1


def test_five_input():
    assert fibonacci(5) == 5


def test_negative_input_exception():
    with pytest.raises(ValueError):
        fibonacci(-1)
