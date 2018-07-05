import unittest

from valid_postal_code import *


class TestPostalCode(unittest.TestCase):


    def test_ok_01(self):
        self.assertTrue(valid_postal_code('12-345'))

    def test_wrong_01(self):
        with self.assertRaises(ValueError):
            valid_postal_code('1-345')


    def test_wrong_02(self):
        with self.assertRaises(ValueError):
            valid_postal_code('12-34')


    def test_wrong_03(self):
        with self.assertRaises(ValueError):
            valid_postal_code('012-345')


    def test_wrong_04(self):
        with self.assertRaises(ValueError):
            valid_postal_code('A2-345')


if __name__ == "__main__":
    unittest.main()
