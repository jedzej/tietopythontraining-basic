import unittest
from the_length_of_the_segment import distance


class MyTest(unittest.TestCase):

    def test_1(self):
        self.assertRaises(TypeError, distance, None, 1, 2, 3)

    def test_2(self):
        self.assertRaises(ValueError, distance, 'aoeu', 1, 2, 3)

    def test_3(self):
        self.assertEqual(distance(1, 1, 1, 1), 0)

    def test_4(self):
        self.assertEqual(distance(-1, -2, -3, -4), 5)

    def test_5(self):
        self.assertEqual(distance(1, 1, 1, 2), 1)

    def test_6(self):
        self.assertEqual(distance(1, 1, 2, 1), 1)

    def test_7(self):
        self.assertEqual(distance(5, 8, 2, 6), 4)

    def test_8(self):
        distance1 = distance(1, 2, 3, 4)
        distance2 = distance(3, 4, 1, 2)
        self.assertEqual(distance1, distance2)


if __name__ == "__main__":
    unittest.main()
