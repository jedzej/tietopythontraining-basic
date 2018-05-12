import unittest
from the_length_of_the_segment import distance

class TestDistance(unittest.TestCase):

    def test_none(self):
        with self.assertRaises(TypeError):
            distance(None, None, None, None)

    def test_string(self):
        with self.assertRaises(TypeError):
            distance('aeou', 'aeou', 'aeou', 'aeou')

    def test_zero(self):
        self.assertEqual(distance(1, 1, 1, 1), 0)

    def test_negative(self):
        self.assertEqual(distance(-1, -1, -2, -2), 1.4142135623730951)

    def test_vertical(self):
        self.assertEqual(distance(1, 1, 1, 2), 1)

    def test_horizontal(self):
        self.assertEqual(distance(1, 1, 2, 1), 1)

    def test_typical(self):
        self.assertEqual(distance(1, 2, 3, 4), 2.8284271247461903)

    def test_order(self):
        self.assertEqual(distance(1, 0, 1, 0), distance(0, 1, 0, 1))

if __name__ == '__main__':
    unittest.main()
