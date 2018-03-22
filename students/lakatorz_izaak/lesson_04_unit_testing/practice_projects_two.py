# Write test module with 3 unit tests for distance() from The length of the
# segment exercise from previous exercise Snakify / Lesson 8 / Problems:

from length_of_segment import distance
import pytest


def test_if_raises_type_error_for_none():
    with pytest.raises(TypeError):
        distance(None)


def test_if_raises_value_error_for_string():
    with pytest.raises(ValueError):
        distance(1, 0, 1, 'aoeu')


def test_corner_cases():
    # Zero length
    assert distance(3, 5, 3, 5) == 0, 'Non-zero value, should be zero.'

    # Negative coordinates
    assert distance(-5, -1, -1, -4) == 5, 'Expected negative coordinates.'

    # Only vertical distance
    assert distance(3, 7, 3, 1) == 6, 'Vertical distance should be equal to 6.'

    # Only horizontal distance
    assert distance(7, 3, 1, 3) == 6, 'Horizontal distance not equal to 6.'

    # Typical conditions
    assert distance(5, 3, 7, 2)

    # Order of points
    assert distance(3, 1, 4, 2) == \
           distance(4, 2, 3, 1), 'Not equal after switching order.'
