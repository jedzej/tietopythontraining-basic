import pytest
from math import sqrt, pow


def distance(x1, y1, x2, y2):
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))


def test_TypeError_case():
    with pytest.raises(TypeError):
        distance()


def test_ValueError_case():
    with pytest.raises(TypeError):
        distance("aoeu")


def test_Zero_Length_case():
    assert distance(1, 1, 1, 1) == 0


def test_Negative_Coordinates():
    assert distance(-2, -2, -1, -1) == sqrt(2)


def test_Only_Vertical_Distance_case():
    assert distance(0, 0, 0, 1) == 1


def test_Only_Horizontal_Distance_case():
    assert distance(0, 0, 1, 0) == 1


def test_Normal_case():
    assert distance(1, 2, 3, 4) == 2 * sqrt(2)


def test_Inverted_Sequence():
    assert distance(1, 2, 3, 4) == distance(3, 4, 1, 2)

