import pytest
from FibonacciNumbers import fibonaczi

class TestFibonaczi:
    def test_Correct_values(self):
        assert fibonaczi(0) == 0
        assert fibonaczi(1) == 1
        assert fibonaczi(6) == 8
        assert fibonaczi(9) == 34
        assert fibonaczi(16) == 987

    def test_Negative_value(self):
        with pytest.raises(RuntimeError) as exception:
            fibonaczi(-3)
        assert 'maximum recursion depth exceeded' in str(exception.value)

    def test_None_Integer_value(self):
        with pytest.raises(TypeError):
            fibonaczi('aoeu')

    def test_None(self):
        with pytest.raises(TypeError):
            fibonaczi(None)
