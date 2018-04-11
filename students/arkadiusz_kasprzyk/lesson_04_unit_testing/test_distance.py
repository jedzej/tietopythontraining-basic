import pytest

import math

epsilon = 1e-13


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


class TestClass(object):

    def test_none(self):
        with pytest.raises(TypeError):
            distance(None, 0, 0, 1)

    def test_value_error(self):
        with pytest.raises(TypeError):
            distance('aoeu', 0, 0, 1)

    def test_corners(self):
        assert math.fabs(distance(0, 0, 0, 0) - 0) < epsilon
        assert distance(-1, -2, -2, -1) > 0
        assert math.fabs(distance(0, 1, 0, 2) - 1) < epsilon
        assert math.fabs(distance(1, 0, 2, 0) - 1) < epsilon

    def test_typical(self):
        assert math.fabs(distance(0, 4, 3, 0) - 5) < epsilon
        assert distance(1, 2, 2, 1) > 0

    def test_order(self):
        assert math.fabs(distance(0, 1, 1, 0) - distance(1, 0, 0, 1)) < epsilon

