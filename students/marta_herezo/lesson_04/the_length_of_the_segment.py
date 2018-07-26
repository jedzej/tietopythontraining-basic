# Given four real numbers: (x1,y1),(x2,y2)//
# calculated distance between two points.

import math
import pytest


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# x1 = float(input("Give x1: "))
# y1 = float(input("Give y1: "))
# x2 = float(input("Give x2: "))
# y2 = float(input("Give y2: "))

# print("Distance between points is: " + str(distance(x1, y1, x2, y2)))

class TestDistance(object):

    def test_none(self):
        with pytest.raises(TypeError):
            distance(None, 0, 0, 0)

    def test_aoeu(self):
        with pytest.raises(ValueError):
            distance('aoeu', 0, 0, 0)

    def test_corner(self):
        assert distance(0, 0, 0, 0) == 0
        assert distance(-1, -2, -3, -4) >= 0
        assert distance(3, 1, 3, 2) == 1
        assert distance(1, 3, 2, 3) == 1

    def test_typical(self):
        assert distance(1, 2, 6, 7) == 8
        assert distance(0, 9, 8, 0) <= 0

    def test_order(self):
        assert distance(1, 1, 0, 0) == distance(0, 0, 1, 1)
