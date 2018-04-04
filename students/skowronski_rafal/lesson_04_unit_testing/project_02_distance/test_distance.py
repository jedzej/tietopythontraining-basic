from mathematics import distance
import pytest
from math import isclose


class TestMathematics():
    test_data_errors = [
        (None, 0, 0, 0, TypeError),
        (0, None, 0, 0, TypeError),
        (0, 0, None, 0, TypeError),
        (0, 0, 0, None, TypeError),

        # distance function should raise 'Type' error when called on 'aoeu'
        # Passing arguments of the wrong type
        # (e.g. passing a list when an int is expected) should result
        # in a TypeError, but passing arguments with the wrong value
        # (e.g. a number outside expected boundaries) should result
        # in a ValueError.
        # see: https://docs.python.org/3/library/exceptions.html
        ('aoeu', 0, 0, 0, TypeError),
        (0, 'aoeu', 0, 0, TypeError),
        (0, 0, 'aoeu', 0, TypeError),
        (0, 0, 0, 'aoeu', TypeError),
    ]

    test_data = [
        (0, 0, 0, 0, 0),
        (-1, 0, -1, 0, 0),
        (-1, -2, -1, -2, 0),
        (-1, -1, -2, -2, 2 ** 0.5),
        (1, 1, 2, 2, 2 ** 0.5),
        (-3, -10, -7, -15, 41 ** 0.5),
        (3, 10, 7, 15, 41 ** 0.5),
        (5, 0, -7, 0, 12),
        (-7, 0, 5, 0, 12),
        (0, 122, 0, -122, 244),
        (0, -122, 0, 122, 244),
        (4, 5, 5, 6, 2 ** 0.5)
    ]

    @pytest.mark.parametrize("x1, y1, x2, y2, error_type", test_data_errors)
    def test_distance_on_exceptions(self, x1, y1, x2, y2, error_type):
        with pytest.raises(error_type):
            distance(x1, y1, x2, y2)

    @pytest.mark.parametrize("x1, y1, x2, y2, expected", test_data)
    def test_distance_with_test_data(self, x1, y1, x2, y2, expected):
        dist = distance(x1, y1, x2, y2)
        assert isclose(dist, expected)
