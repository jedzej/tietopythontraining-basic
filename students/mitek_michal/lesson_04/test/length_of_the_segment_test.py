import pytest
from lesson_04.src.length_of_the_segment import \
    calculate_length_of_the_segment


def test_length_of_the_segment_raises_type_error_when_none_provided():
    with pytest.raises(TypeError):
        calculate_length_of_the_segment(None, None, None, None)


def test_length_of_the_segment_raises_value_error_when_string_provided():
    with pytest.raises(ValueError):
        calculate_length_of_the_segment('aoeu', 'aoeu', 'aoeu', 'aoeu')


def test_length_of_segment_raises_value_error_when_one_argument_is_string():
    with pytest.raises(ValueError):
        calculate_length_of_the_segment('1', 2, 3, 4)


def test_length_of_the_segment_returns_zero_distance_when_called_on_zero():
    assert calculate_length_of_the_segment(0, 0, 0, 0) == 0


def test_length_of_the_segment_on_vertical_distance():
    assert calculate_length_of_the_segment(1, 3, 1, 10) == 7


def test_length_of_the_segment_on_horizontal_distance():
    assert calculate_length_of_the_segment(2, 1, -2, 1) == 4


def test_length_of_the_segment():
    assert calculate_length_of_the_segment(-7, -4, 10, 3) == 18.384776310850235


def test_length_of_the_segment_if_works_with_switched_order_of_points():
    assert calculate_length_of_the_segment(10, 3, -7, -4) == 18.384776310850235
