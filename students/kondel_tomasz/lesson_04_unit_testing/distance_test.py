import pytest
import sys
sys.path.insert(0, '../lesson_03_funtions/')
from the_length_of_the_segment import distance  # noqa: E402


def test_crash_with_TypeError():
    with pytest.raises(TypeError):
        (distance(None, 0, 0, 0))


def test_crash_with_ValueError():
    with pytest.raises(ValueError):
        (distance('aoeu', 0, 0, 0))


def test_zero_length():
    assert(distance(0, 0, 0, 0) == 0)


def test_negative_coordinates():
    assert(distance(-5, -5, -3, -5) > 0)


def test_only_vertical_distance():
    assert(distance(0, 5, 0, 2) == 3)


def test_only_horizontal_distance():
    assert(distance(0, 3, 10, 3) == 10)


def test_typical_points():
    assert(distance(1, 1, 2, 2) > 1.2)


def test_reverse_order():
    assert(distance(5, 6, 13, 15) == distance(13, 15, 5, 6))
