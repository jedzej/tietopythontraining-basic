import math
import unittest
import pytest
from length_of_the_segment import distance


class TestDistanceFunction(unittest.TestCase):

    def test_input_none(self):
        with pytest.raises(TypeError):
            distance(None)

    def test_input_string(self):
        with pytest.raises(TypeError):
            distance('aoeu')

    def test_zero_distance(self):
        self.assertEqual(distance(1, 1, 1, 1), 0, "zero distance")

    def test_corner_cases(self):
        self.assertEqual(distance(-1, -1, -2, -2), math.sqrt(2), "test \
        negative coordinates")
        self.assertEqual(distance(0, 1, 0, 2), 1, "test only vertical")
        self.assertEqual(distance(1, 0, 2, 0), 1, "test only horizontal")

    def test_typical_conditions(self):
        self.assertEqual(distance(1, 2, 3, 4), math.sqrt(8), "typical")

    def test_order_of_points(self):
        self.assertEqual(distance(1, 2, 3, 4), distance(3, 4, 1, 2), "order 1")
        self.assertEqual(distance(5, 6, 7, 8), distance(7, 8, 5, 6), "order 2")


if __name__ == '__main__':
    unittest.main()
