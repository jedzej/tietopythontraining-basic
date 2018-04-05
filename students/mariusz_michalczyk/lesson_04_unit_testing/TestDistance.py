import unittest
import The_length_of_the_segment


class TestDistanceFunction(unittest.TestCase):
    def test_type_error_when_string_entered(self):
        with self.assertRaises(TypeError):
            The_length_of_the_segment.distance("shit")

    def test_type_error_when_none_entered(self):
        with self.assertRaises(TypeError):
            The_length_of_the_segment.distance(None)

    def test_zero_length(self):
        self.assertEqual(The_length_of_the_segment.distance(0, 0, 0, 0), 0)

    def test_negative_coordinates(self):
        self.assertEqual(The_length_of_the_segment.distance(-1, -1, -1, -1), 0)
        self.assertEqual(The_length_of_the_segment.distance(-1, 0, 0, 0), 1)

    def test_only_vertical_distance(self):
        with self.assertRaises(TypeError):
            The_length_of_the_segment.distance(None, 1, None, 2)

    def test_only_horizontal_distance(self):
        with self.assertRaises(TypeError):
            The_length_of_the_segment.distance(1, None, 1, None)

    def test_typical_conditions(self):
        self.assertEqual(The_length_of_the_segment.distance(2, 2, 3, 3), 1.4142135623730951)
        self.assertEqual(The_length_of_the_segment.distance(3, 1, 3, 1), 0)
        self.assertEqual(The_length_of_the_segment.distance(3, 0, 3, 1), 1)


if __name__ == '__main__':
    unittest.main()
