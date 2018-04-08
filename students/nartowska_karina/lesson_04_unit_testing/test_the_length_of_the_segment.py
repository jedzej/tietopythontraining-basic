import unittest
from lesson_03_functions.the_length_of_the_segment import distance


class MyTest(unittest.TestCase):
    def test_type_error_when_called_on_none(self):
        self.assertRaises(TypeError, distance, None)

    def test_value_error_when_called_on_aoeu(self):
        self.assertRaises(TypeError, distance, 'aoeu')

    def test_zero_length(self):
        self.assertEqual(distance(5, 5, 5, 5), 0)

    def test_negative_coordinates(self):
        self.assertEqual(distance(-3, 5, -1, 5), 2)

    def test_only_vertical_distance(self):
        self.assertEqual(distance(0, 5, 0, 1), 4)

    def test_only_horizontal_distance(self):
        self.assertEqual(distance(5, 0, 1, 0), 4)

    def test_typical_conditions(self):
        self.assertEqual(distance(9, 5, 5, 2), 5)

    def test_the_order_of_point_does_not_matter(self):
        self.assertEqual(distance(9, 5, 5, 2), distance(5, 2, 9, 5))


if __name__ == "__main__":
    unittest.main()
