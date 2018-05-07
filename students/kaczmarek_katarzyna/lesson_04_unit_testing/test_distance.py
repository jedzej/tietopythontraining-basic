import pytest
from the_length_of_the_segment import distance


def test_crash_with_type_error_on_none():
    with pytest.raises(TypeError):
        distance(None, None, None, None)


def test_crash_with_value_error_on_aoeu():
    with pytest.raises(ValueError):
        distance('aoeu', 'aoeu', 'aoeu', 'aoeu')


def test_zero_length():
    assert distance(5, 5, 5, 5) == 0.0


def test_negative_coordinates():
    assert distance(-1, -1, -1, -2) == 1.0


def test_only_vertical_distance():
    assert distance(0, 1, 0, 4) == 3.0


def test_only_horizontal_distance():
    assert distance(1, 0, 4, 0) == 3.0


def test_typical_conditions():
    assert distance(2, 6, 4, -9) == 15.132745950421556


def test_order_does_not_matter():
    assert distance(4, -3, -5, 2) == distance(-5, 2, 4, -3)
