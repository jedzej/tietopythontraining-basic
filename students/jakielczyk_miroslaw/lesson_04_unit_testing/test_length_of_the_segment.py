import pytest
from length_of_the_segment import distance


def test_type_error():
    with pytest.raises(TypeError):
        distance(None)


def test_value_error():
    with pytest.raises(TypeError):
        distance('aoeu', 1, 5, 4)


def test_zero_length():
    assert distance(0, 0, 0, 0) == 0
    assert distance(-5, -5, -5, -5) == 0
    assert distance(1.5, 1.5, 1.5, 1.5) == 0


def test_negative_coordinates():
    assert distance(-1, -1, -4, -5) == 5
    assert distance(-10.1, -10.1, -5.1, -5.1) == 7.0710678118654755


def test_vertical_distance():
    assert distance(3, 3, 3, 10) == 7
    assert distance(-3, -3, -3, 3.5) == 6.5


def test_horizontal_distance():
    assert distance(0, 5, 10, 5) == 10


def test_mixed_coordinates():
    assert distance(-2.5, 2.5, 0.5, 6.5) == 5
    assert distance(2, 2, 7.5, 5) == 6.264982043070834


def test_order_of_points():
    assert distance(-2.5, 2.5, 0.5, 6.5) == distance(0.5, 6.5, -2.5, 2.5)
