import math
import unittest


def distance(x1, y1, x2, y2):
    if x1 is str or y1 is str or x2 is str or y2 is str:
        raise ValueError
    else:
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def point_order(x1, y1, x2, y2):
        if distance(x1, y1, x2, y2) == distance(x2, y2, x1, y1):
            return 0
        else:
            return None


class MyTest(unittest.TestCase):

    def test_type_error_with_pytest_raises(self):
        self.assertRaises(TypeError, distance, None)

    def test_zero_length(self):
        self.assertEqual(distance(2, 2, 2, 2), 0)

    def test2(self):
        self.assertRaises(TypeError, distance, 'aoeu', 2, 3, 5)

    def test_negative_coordinates(self):
        self.assertEqual(distance(-2, -1, 1, 3), 5)

    def test_only_vertical_distance(self):
        self.assertEqual(distance(1, 1, 1, 3), 2)

    def test_only_horizontal_distance(self):
        self.assertEqual(distance(1, 1, 3, 1), 2)

    def test_typical_conditions(self):
        self.assertEqual(distance(1, 1, 4, 5), 5)

    def test_order_of_points_does_not_matter(self):
        self.assertEqual(point_order(1, 1, 4, 5), 0)


if __name__ == '__main__':
    unittest.main()
