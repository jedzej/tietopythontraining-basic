# tests for distance.py
import unittest
import distance


class DistanceTest(unittest.TestCase):

    # Tests that it crashes with TypeError when called on None
    def test_None_all(self):
        self.assertIsNotNone(TypeError,
                             distance.distance(None, None, None, None))

    def test_None_x1(self):
        self.assertIsNotNone(TypeError, distance.distance(None, 2, 3, 2))

    def test_None_y1(self):
        self.assertIsNotNone(TypeError, distance.distance(1, None, 3, 2))

    def test_None_x2(self):
        self.assertIsNotNone(TypeError, distance.distance(1, 2, None, 2))

    def test_None_y2(self):
        self.assertIsNotNone(TypeError, distance.distance(2, 3, 2, None))

    # Tests that it crashes with ValueError when called on 'aoeu'
    def test_string_all(self):
        self.assertRaises(ValueError, distance.distance('aoeu', 'aoeu', 'aoeu', 'aoeu'))

    def test_string_x1(self):
        self.assertRaises(ValueError, distance.distance('aoeu', 2, 3, 2))

    def test_string_y1(self):
        self.assertRaises(ValueError, distance.distance(2, 'aoeu', 3, 2))

    def test_string_x2(self):
        self.assertRaises(ValueError, distance.distance(2, 3, 'aoeu', 2))

    def test_string_y222(self): # why stickler doesn't see func. changes in 32 line?
        self.assertRaises(ValueError, distance.distance(2, 3, 2, 'aoeu'))

    # Tests it on corner cases:
    def test_vaule_zero(self):
        self.assertEqual(distance.distance(2, 1, 2, 1), 0.0) # Zero length

    def test_vaule_negative(self):
        self.assertEqual(distance.distance(-1, -1, -3, -5),
                         4.47214)  # Negative coordinates

    def test_vaule_vertical(self):
        self.assertEqual(distance.distance(2, 1, 2, 7),
                         6.0)  # Only vertical distance

    def test_vaule_horizontaly(self):
        self.assertEqual(distance.distance(5, 1, 10, 1),
                         5.0)  # Only horizontal distance

    # Typical conditions (difference on both coordinates)
    def test_vaule_1(self):
        self.assertEqual(distance.distance(3, -2, -1, 7), 9.84886)

    def test_vaule_2(self):
        self.assertEqual(distance.distance(-10, 2, 5, 12), 18.02776)

    def test_vaule_3(self):
        self.assertEqual(distance.distance(1, -5, -10, -12), 13.0384)

    # Test that the order of points does not matter
    def test_order(self):
        self.assertEqual(distance.distance(5, 1, 10, 2),
                         distance.distance(10, 2, 5, 1))


if __name__ == '__main__':
    unittest.main()
