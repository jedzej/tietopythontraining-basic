import unittest


def distance(x1, y1, x2, y2):
    result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return result


class TestDistance(unittest.TestCase):

    def test_raises_type_error(self):
        s = None
        with self.assertRaises(TypeError):
            distance(s, 2, 3, 4)

    def test_raises_value_error(self):
        s = 'aoeu'
        with self.assertRaises(TypeError):
            distance(s, 1, 2, 3)

    def test_zero_length(self):
        self.assertEqual(distance(1, 0, 1, 0), 0)

    def test_negative_coordinates(self):
        self.assertEqual(distance(-1, -2, -3, -4), 2.8284271247461903)

    def test_only_vertical_distance(self):
        self.assertEqual(distance(1, 1, 1, 4), 3.0)

    def test_only_horizontal_distance(self):
        self.assertEqual(distance(1, 1, 4, 1), 3.0)

    def test_typical_conditions(self):
        self.assertEqual(distance(8, 6, 4, 2), 5.656854249492381)

    def test_order_of_points(self):
        dist1 = distance(2, 4, 6, 8)
        dist2 = distance(6, 8, 2, 4)
        self.assertEqual(dist1, dist2)


if __name__ == '__main__':
    unittest.main()