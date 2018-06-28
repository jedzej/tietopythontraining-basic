import pytest
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class TestClass(object):

    def test_distance_none(self):
        with pytest.raises(TypeError):
            distance(None, None, None, None)

    def test_distance_aoeu(self):
        with pytest.raises(TypeError):
            distance('aoeu')

    def test_distance_0(self):
        assert distance(0, 0, 0, 0) == 0

    def test_distance_negative(self):
        assert distance(-1, -1, -4, -5) == 5.0

    def test_distance_vertical(self):
        assert distance(1, 1, 1, -5) == 6

    def test_distance_horizontal(self):
        assert distance(-1, -1, -4, -1) == 3

    def test_distance_order(self):
        assert distance(1, 2, 4, 4) == distance(4, 4, 1, 2)


if __name__ == '__main__':
    pytest.main()
