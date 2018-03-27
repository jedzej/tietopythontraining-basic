import pytest
from the_length_of_the_segment import distance


def test_none_input():
    with pytest.raises(TypeError):
        distance(None, None, None, None)


def test_aoeu_input():
    with pytest.raises(TypeError):
        distance('aoeu', 'aoeu', 'aoeu', 'aoeu')


def test_zero_length():
    assert distance(1, 1, 1, 1) == 0


def test_negative_values():
    assert distance(-3, -4, 0, 0) == 5


def test_vertical_only():
    assert distance(0, 1, 0, 6) == 5


def test_horizontal_only():
    assert distance(1, 0, 6, 0) == 5


def test_typical_points():
    assert distance(4, 5, 1, 1) == 5


def test_if_order_of_points_matters():
    assert distance(1, 2, 3, 4) == distance(4, 3, 2, 1)
