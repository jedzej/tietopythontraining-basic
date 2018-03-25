import unittest
from math import sqrt


def distance(x1, y1, x2, y2):
    if x1 is str or y1 is str or x2 is str or y2 is str:
        raise ValueError
    else:
        return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def main():
    print("Enter four real numbers representing cartesian coordinates")
    print("x1 is: ")
    x1 = float(input())
    print("y1 is: ")
    y1 = float(input())
    print("x2 is: ")
    x2 = float(input())
    print("y2 is: ")
    y2 = float(input())
    print("The distance is:")
    distance(x1, y1, x2, y2)


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
