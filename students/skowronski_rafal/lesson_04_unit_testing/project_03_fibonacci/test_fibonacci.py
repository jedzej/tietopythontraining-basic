from fibonacci import fibonacci
import pytest


class TestFibonacci():
    error_prone_values = [
        ('foo', TypeError),
        (2.45, TypeError),
        ([], TypeError),
        (0, ValueError),
        (False, ValueError),
        (-1, ValueError),
        (-123, ValueError)
    ]

    positives = [
        (True, 1),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (8, 21),
        (12, 144),
        (15, 610)
    ]

    @pytest.mark.parametrize('n, value', error_prone_values)
    def test_fibonacci_on_error_prone(self, n, value):
        with pytest.raises(value):
            fibonacci(n)

    @pytest.mark.parametrize('n, value', positives)
    def test_fibonacci_on_positives(self, n, value):
        assert fibonacci(n) == value
