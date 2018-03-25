import unittest

from the_length_of_the_segment import calculate_distance


class TestDistance(unittest.TestCase):
    def testNoneCoordinate(self):
        with self.assertRaises(TypeError):
            calculate_distance(1, 5, 1, None)

    def testStringCoordinate(self):
        with self.assertRaises(TypeError):
            calculate_distance(1, 5, 1, "aeou")

    def testZeroCoordinate(self):
        self.assertTrue(calculate_distance(0, 1, 10, 0) > 0)

    def testNegativeCoordinate(self):
        self.assertTrue(calculate_distance(1, -3.54, -4, -22) > 0)

    def testVerticalDisatance(self):
        self.assertTrue(calculate_distance(0, 0, 0, 10) > 0)

    def testHorizontalDistance(self):
        self.assertTrue(calculate_distance(0, -4, 10, -4) > 0)

    def testReversedCoordinates(self):
        self.assertEquals(calculate_distance(1, 4, 7, 2),
                          calculate_distance(4, 1, 2, 7))


if __name__ == '__main__':
    unittest.main()
