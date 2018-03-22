#!/usr/bin/env python3

# Run with:
# pytest distance_tests.py

import pytest
import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/lesson_03_functions")

from the_length_of_the_segment import distance


def test_distance_from_the_same_point_to_the_same_point_is_zero():
    assert distance(1, 2, 1, 2) == 0
    assert distance(0, 0, 0, 0) == 0


def test_coordinates_sign_does_not_influence_distance():
    assert distance(-1, -2, -3, -4) == distance(1, 2, 3, 4)


def test_distance_of_points_on_the_same_line_is_equal_to_line_length():
    assert distance(0, 0, 0, 7) == 7
    assert distance(0, 0, 7, 0) == 7


def test_that_order_of_points_does_not_matter():
    assert distance(5, 6, 7, 8) == distance(7, 8, 5, 6)


def test_distance_raises_type_error_with_invalid_input():
    with pytest.raises(TypeError):
            distance('aoeu', 0, 0, 0)

    with pytest.raises(TypeError):
            distance(None, 0, 0, 0)
