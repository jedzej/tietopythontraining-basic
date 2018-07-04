import unittest
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class MyTest(unittest.TestCase):

    def test_distance_none(self):
        self.assertRaises(TypeError, distance, None)

    def test_distance_aoeu(self):
        self.assertRaises(TypeError, distance, 'aoeu')

    def test_distance_0(self):
        self.assertEqual(distance(0, 0, 0, 0), 0)

    def test_distance_negative(self):
        self.assertEqual(distance(-1, -1, -4, -5), 5.0)

    def test_distance_vertical(self):
        self.assertEqual(distance(1, 1, 1, -5), 6)

    def test_distance_horizontal(self):
        self.assertEqual(distance(-1, -1, -4, -1), 3)

    def test_distance_order(self):
        self.assertEqual(distance(1, 2, 4, 4), distance(4, 4, 1, 2))


if __name__ == '__main__':
    unittest.main()
