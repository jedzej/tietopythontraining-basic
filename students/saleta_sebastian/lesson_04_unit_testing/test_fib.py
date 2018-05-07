import pytest

from lesson_03_functions.fib import fib


@pytest.mark.parametrize("test_input, expected", [
    (1, 1),
    (2, 1),
    (3, 2),
    (10, 55)
])
def test_if_fib_return_expected_value(test_input, expected):
    assert fib(test_input) == expected


def test_if_return_type_error_when_wrong_input():
    with pytest.raises(TypeError):
        fib("python monty pythons")


def test_if_call_runtime_error_when_negative_value():
    with pytest.raises(RuntimeError) as error_info:
        fib(-3)
        assert error_info.value.message == 'maximum recursion depth exceeded'
