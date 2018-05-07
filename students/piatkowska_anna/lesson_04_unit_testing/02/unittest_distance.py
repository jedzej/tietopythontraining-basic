"""
Write test module with 3 unit tests for distance() from
The length of the segment exercise from previous exercise
Snakify / Lesson 8 / Problems:

Test that it crashes with TypeError when called on None (use pytest.raises),
Test that it crashes with ValueError when called on 'aoeu',
Test it on corner cases:
Zero length,
Negative coordinates,
Only vertical distance,
Only horizontal distance,
Typical conditions (difference on both coordinates),
Test that the order of points does not matter.
"""
import length_of_the_segment as len
import pytest


def test_raises_type_error_when_called_on_None():
    with pytest.raises(TypeError):
        len.distance(None)


def test_raises_value_error_when_called_on_aoeu():
    with pytest.raises(ValueError):
        len.distance("aoeu", 2, 2, 2)


def test_returns_0_for_the_same_point():
    assert len.distance(3, 3, 3, 3) == 0


def test_returns_proper_distance_for_negative_coordinates():
    assert len.distance(-6, -2, -8, -2) == 2


def test_return_proper_distance_for_vertical_distance():
    assert len.distance(0, 2, 0, 7) == 5


def test_return_proper_distance_for_horizontal_distance():
    assert len.distance(2, 0, 7, 0) == 5


def test_return_proper_distance_for_typical_coordinates():
    assert len.distance(2, 5, 5, 9) == 5


def test_return_same_distance_when_poits_are_switched():
    assert len.distance(3, 2, 4, 7) == len.distance(4, 7, 3, 2)
