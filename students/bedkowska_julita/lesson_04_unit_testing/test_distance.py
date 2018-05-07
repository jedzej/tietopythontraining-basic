import pytest


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# TESTS

def test_None_value():
    with pytest.raises(TypeError):
        distance(None, None, None, None)


def test_String_value():
    with pytest.raises(TypeError):
        distance('aoeu', '1', '1', '1')


def test_zero_length():
    assert distance(1, 1, 1, 1) == 0


def test_negative():
    assert distance(-1, -2, -3, -2) == 2.0


def test_only_vertical():
    assert distance(1, 4, 1, 1) == 3


def test_only_horizontal():
    assert distance(1, 1, 6, 1) == 5


def test_typical_coordinates():
    assert distance(1, 5, 6, 13) == 9.433981132056603


def test_points_order():
    distance1 = distance(1, 2, 3, 4)
    distance2 = distance(4, 3, 2, 1)
    assert distance1 == distance2
