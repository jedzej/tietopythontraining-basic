import unittest, pytest
from distance_to_test import distance


class test_that_distance_fail(unittest.TestCase):
    def test_zero_length(self):
        with pytest.raises(TypeError):
            distance(0, None, 0, 0)
        raise Exception('Bad value')

    def test_value_error(self):
        try:
            self.assertEqual(distance(0, 0, 0, 0), 0)
        except ValueError as err:
            print(err.args)

    def test_negative_value(self):
        try:
            self.assertEqual(distance(-2, -2, -2, -2), 0)
        except ValueError as err:
            print(err.args)

    def test_only_vertical(self):
        try:
            self.assertEqual(distance(5, 0, 10, 0), 5)
        except ValueError as err:
            print(err.args)

    def test_only_horizontal(self):
        try:
            self.assertEqual(distance(0, 5, 0, 10), 5)
        except ValueError as err:
            print(err.args)

    def test_when_distance_equals_zero(self):
        try:
            self.assertEqual(distance(4, 1, 4, 1), 0)
        except ValueError as err:
            print(err.args)

if __name__ == '__main__':
    unittest.main()
