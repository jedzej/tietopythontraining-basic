import sys
import unittest
from lesson_03_functions.the_length_of_the_segment import distance
sys.path.append('..')


class TestDistance(unittest.TestCase):
    def test_on_none(self):
        self.assertRaises(TypeError, distance, None, 1, 2, 3)

    def test_non_integer(self):
        self.assertRaises(TypeError, distance, 'aoeu', 1, 2, 3)

    def test_zero_length(self):
        self.assertEqual(distance(2, 2, 2, 2), 0)

    def test_negative_coordinates(self):
        self.assertEqual(distance(-2, -7, -13, -1), 12.529964086141668)

    def test_vertical_distance(self):
        self.assertEqual(distance(2, 2, 2, 12), 10)

    def test_horizontal_distance(self):
        self.assertEqual(distance(2, 2, 12, 2), 10)

    def test_typical_coordinates(self):
        self.assertEqual(distance(2, 3, 12, 4), 10.04987562112089)

    def test_points_order(self):
        distance1 = distance(1, 2, 3, 4)
        distance2 = distance(3, 4, 1, 2)
        self.assertEqual(distance1, distance2)


if __name__ == '__main__':
    unittest.main()
