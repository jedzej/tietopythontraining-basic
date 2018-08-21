import unittest

from valid_postal_code import *


class TestPostalCode(unittest.TestCase):


    def test_00_ok(self):
        self.assertTrue(valid_postal_code('12-345'))

    def test_01_prefix_too_short(self):
        with self.assertRaises(ValueError):
            valid_postal_code('1-345')


    def test_02_suffux_too_short(self):
        with self.assertRaises(ValueError):
            valid_postal_code('12-34')


    def test_03_prefix_too_long(self):
        with self.assertRaises(ValueError):
            valid_postal_code('012-345')


    def test_04_letter(self):
        with self.assertRaises(ValueError):
            valid_postal_code('A2-345')


if __name__ == "__main__":
    unittest.main()
