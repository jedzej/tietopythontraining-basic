import pytest


def distance(x1, y1, x2, y2):
    result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return result


def test_raises_type_error():
    s = None
    with pytest.raises(TypeError):
        distance(s, 2, 3, 4)


def test_raises_value_error():
    s = 'aoeu'
    with pytest.raises(TypeError):
        distance(s, 1, 2, 3)


def test_zero_length():
    assert distance(1, 0, 1, 0) == 0


def test_negative_coordinates():
    assert distance(-1, -2, -3, -4) == 2.8284271247461903


def test_only_vertical_distance():
    assert distance(1, 1, 1, 4) == 3.0


def test_only_horizontal_distance():
    assert distance(1, 1, 4, 1) == 3.0


def test_typical_conditions():
    assert distance(2, 3, 12, 4) == 10.04987562112089


def test_order_of_points():
    dist1 = distance(1, 2, 3, 4)
    dist2 = distance(3, 4, 1, 2)
    assert dist1 == dist2
