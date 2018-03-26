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
        distance = calculate_distance(0, 1, 10, 0)
        self.assertTrue(
                math.isclose(distance, 10.04987562112089, rel_tol=1e-09))

    def testNegativeCoordinate(self):
        distance = calculate_distance(1, -3.54, -4, -22)
        self.assertTrue(
                math.isclose(distance, 18.563717300153005, rel_tol=1e-09))

    def testVerticalDisatance(self):
        distance = calculate_distance(0, 0, 0, 10)
        self.assertTrue(
                math.isclose(distance, 10, rel_tol=1e-09))

    def testHorizontalDistance(self):
        distance = calculate_distance(0, -4, 10, -4)
        self.assertTrue(
                math.isclose(distance, 14.560219778561036, rel_tol=1e-09))

    def testReversedCoordinates(self):
        self.assertEquals(calculate_distance(1, 4, 7, 2),
                          calculate_distance(4, 1, 2, 7))


if __name__ == '__main__':
    unittest.main()
