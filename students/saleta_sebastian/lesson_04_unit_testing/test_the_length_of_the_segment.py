import pytest

from lesson_03_functions.the_length_of_the_segment import print_distance


def test_if_distance_return_tupe_error_for_coordinates_are_none():
    with pytest.raises(TypeError):
        print_distance(None, None, None, None)


def test_if_distance_return_type_error_for_wrong_input_value():
    with pytest.raises(TypeError):
        print_distance('aoeu', 1, 1, 1)


def test_zero_length_value():
    assert print_distance(0, 0, 0, 0) == 0


def test_if_distance_is_correct_when_coordinates_are_negative():
    assert pytest.approx(print_distance(-10, -14, -3, -2), 0.01) == 14


def test_if_distance_is_correct_when_coordinates_are_vertical():
    assert print_distance(2, 4, 2, 6) == 2


def test_if_distance_is_correct_when_coordinates_are_horizontal():
    assert print_distance(4, 5, 2, 5) == 2


def test_if_distance_is_the_same_for_different_order_of_points():
    assert print_distance(1, 5, 5, 8) == print_distance(5, 8, 1, 5)


def test_if_distance_is_correct_for_typical_conditions():
    assert pytest.approx(print_distance(1, 2, 3, 4), 0.01) == 2.82
