from fibonacci_numbers import fibonacci
import pytest


@pytest.mark.parametrize("test_input, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (6, 8),
])
def test_eval(test_input, expected):
    assert fibonacci(test_input) == expected


def test_none_input_exception():
    with pytest.raises(TypeError):
        fibonacci(None)


def test_aoeu_input_exception():
    with pytest.raises(TypeError):
        fibonacci('aoeu')


def test_negative_input_exception():
    with pytest.raises(ValueError):
        fibonacci(-1)
