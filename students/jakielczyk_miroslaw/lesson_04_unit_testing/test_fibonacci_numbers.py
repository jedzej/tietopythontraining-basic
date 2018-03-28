import pytest
from fibonacci_numbers import fibonaczi


class TestFibonaczi:
    def test_correct_values(self):
        assert fibonaczi(0) == 0
        assert fibonaczi(1) == 1
        assert fibonaczi(6) == 8
        assert fibonaczi(9) == 34
        assert fibonaczi(16) == 987

    def test_negative_value(self):
        with pytest.raises(RuntimeError) as exception:
            fibonaczi(-3)
        assert 'maximum recursion depth exceeded' in str(exception.value)

    def test_none_integer_value(self):
        with pytest.raises(TypeError):
            fibonaczi('aoeu')

    def test_none(self):
        with pytest.raises(TypeError):
            fibonaczi(None)
