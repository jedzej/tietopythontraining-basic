import pytest
from the_length_of_the_segment import distance


def test_type_error_none():
    with pytest.raises(TypeError):
        distance(None, None, None, None)


def test_value_error_string():
    with pytest.raises(TypeError):
        distance('aoeu', 'aoeu', 'aoeu', 'aoeu')


def test_zero_length():
    assert distance(1, 1, 1, 1) == 0.0


def test_negative():
    assert distance(-1, -1, -1, -1) == 0.0


def test_only_vertical_distance():
    assert distance(1, 1, 1, 2) == 1.0


def test_only_horizontal_distance():
    assert distance(1, 1, 2, 1) == 1.0


def test_typical_conditions():
    assert distance(3, 5, 7, 9) == 5.656854249492381


def test_order_does_not_matter():
    assert distance(3, 5, 7, 9) == distance(7, 9, 3, 5)
