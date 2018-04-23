import pytest
from math import sqrt


def distance(a1, b1, a2, b2):
    return sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)


class MyTest(object):


    def test_none_value(self):
        with pytest.raises(TypeError):
            distance(None, None, None, None)

    def test_String_value(self):
        with pytest.raises(TypeError):
            distance('aoeu', 'aoeu', 'aoeu', 'aoeu')

    def test_zero_length(self):
        assert distance(5, 5, 5, 5) == 0

    def test_negative(self):
        assert distance(-1, -2, -3, -2) == 2.0

    def test_only_vertical(self):
        assert distance(1, 4, 1, 1) == 3

    def test_only_horizontal(self):
        assert distance(1, 1, 6, 1) == 5

    def test_typical_coordinates(self):
        assert distance(1, 5, 6, 13) == 9.433981132056603

    def test_points_order(self):
        distance1 = distance(1, 2, 3, 4)
        distance2 = distance(4, 3, 2, 1)
        assert distance1 == distance2
