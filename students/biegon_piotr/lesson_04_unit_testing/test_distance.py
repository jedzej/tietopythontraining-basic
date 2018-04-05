import unittest
import pytest
from distance_of_the_segment import distance


class TestDistanceFunction(unittest.TestCase):

    def test_TypeError_when_input_is_None(self):
        with pytest.raises(TypeError):
            distance(None)

    def test_ValueError_when_input_is_string(self):
        with pytest.raises(ValueError):
            distance("aoeu", 1, 1, 1)

    def test_zero_length(self):
        self.assertEqual(0, distance(1, 1, 1, 1))

    def test_negative_coordinates(self):
        self.assertEqual(2, distance(-1, -1, -1, -3))

    def test_only_vertical_distance(self):
        self.assertEqual(2, distance(1, 1, 1, 3))

    def test_only_horizontal_distance(self):
        self.assertEqual(2, distance(1, 1, 3, 1))

    def test_typical_conditions(self):
        self.assertAlmostEqual(2.82, distance(1, 2, 3, 4), places=1)

    def test_order_of_point_does_not_matter(self):
        self.assertEqual(distance(1, 2, 3, 4), distance(3, 4, 1, 2))
