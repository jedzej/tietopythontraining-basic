import pytest
from the_length_of_segment import distance


def test_type_error():
    with pytest.raises(TypeError):
        distance('aoeu')


def test_value_error():
    with pytest.raises(TypeError):
        distance(None)


def test_zero_length():
    assert distance(1, 1, 1, 1) == 0


def test_negative_coordinates():
    assert round(distance(-2, -3, -10, 8), 4) == 13.6015


def test_vertical_distance():
    assert distance(0, 5, 0, 0) == 5


def test_horizontal_distance():
    assert distance(0, 0, 10, 0) == 10


def test_order():
    assert distance(1, 2, 3, 4) == distance(3, 4, 1, 2)


def test_typical():
    assert round(distance(2, 3, 10, 8), 4) == 9.434
