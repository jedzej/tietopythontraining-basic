#!/usr/bin/env python3

"""
ut_distance.py: Unit tests for distance() function  from
"The length of the segment" exercise
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import pytest
from snakify_lesson8 import distance


class TestDistance(object):

    def test_type_error(self):
        with pytest.raises(TypeError):
            distance(None, 1.2, 3.4, 5.6)

    def test_value_error(self):
        with pytest.raises(ValueError):
            distance('aeou', 1.2, 3.4, 5.6)

    def test_zero_length(self):
        result = distance(1.2, 3.4, 1.2, 3.4)
        assert self.are_floats_equal(result, 0.0)

    def test_negative_coordinates(self):
        result = distance(-1.2, -3.4, -5.6, -7.8)
        assert self.are_floats_equal(result, 6.22254)

    def test_vertical_distance(self):
        result = distance(1.2, 3.4, 1.2, 5.6)
        assert self.are_floats_equal(result, 2.2)

    def test_horizontal_distance(self):
        result = distance(1.2, 3.4, 5.6, 3.4)
        assert self.are_floats_equal(result, 4.4)

    def test_typical_values(self):
        result = distance(1.2, 3.4, 5.6, 7.8)
        assert self.are_floats_equal(result, 6.22254)

    def test_order_of_points(self):
        dist_1 = distance(1.2, 3.4, 5.6, 7.8)
        dist_2 = distance(5.6, 7.8, 1.2, 3.4)
        assert self.are_floats_equal(dist_1, dist_2)

    @staticmethod
    def are_floats_equal(num1, num2, threshold=0.00001):
        if abs(num1 - num2) < threshold:
            return True
        else:
            return False


if __name__ == '__main__':
    pytest.main()
