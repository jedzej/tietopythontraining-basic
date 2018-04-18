import pytest


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


class TestClass(object):

    def test_none(self):
        with pytest.raises(TypeError):
            distance(None, 0, 0, 1)

    def test_value_error(self):
        with pytest.raises(ValueError):
            distance('aoeu', 0, 0, 1)

    def test_corners(self):
        assert distance(0, 0, 0, 0) == 0
        assert distance(-1, -2, -2, -1) > 0
        assert distance(0, 1, 0, 2) == 1
        assert distance(1, 0, 2, 0) == 1

    def test_typical(self):
        assert distance(0, 4, 3, 0) == 5
        assert distance(1, 2, 2, 1) > 0

    def test_order(self):
        assert distance(0, 1, 1, 0) == distance(1, 0, 0, 1)
