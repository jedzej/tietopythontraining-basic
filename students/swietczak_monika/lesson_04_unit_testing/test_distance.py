import pytest
from math import sqrt


def distance(x1, y1, x2, y2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class TestClass(object):
    def test_type(self):
        with pytest.raises(TypeError):
            distance(None, None, None, None)

    def test_value(self):
        with pytest.raises(ValueError):
            distance('aoeu', 'aoeu', 'aoeu', 'aoeu')

    def test_zero_length(self):
        assert distance(0, 0, 0, 0) == 0

    def test_negative(self):
        assert distance(-1, -1, -3, -1) == 2

    def test_horizontal(self):
        assert distance(2, 0, 0, 0) == 2

    def test_vertical(self):
        assert distance(0, 2, 0, 0) == 2

    def test_standard(self):
        assert distance(1, 3, 2, 5) == pytest.approx(2.2, 0.1)

    def test_order(self):
        assert distance(1, 3, 2, 5) == distance(2, 5, 1, 3)
