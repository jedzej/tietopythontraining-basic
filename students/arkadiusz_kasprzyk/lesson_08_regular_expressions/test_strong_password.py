import unittest

from strong_password import *


class TestStrongPassword(unittest.TestCase):


    def test_01_too_short(self):
        with self.assertRaises(ValueError):
            strong_password('seVen77')


    def test_02_only_lower(self):
        with self.assertRaises(ValueError):
            strong_password('abcdefgh')


    def test_03_only_upper(self):
        with self.assertRaises(ValueError):
            strong_password('ABCDEFGH')


    def test_04_no_numbers(self):
        with self.assertRaises(ValueError):
            strong_password('Abcdefgh')


    def test_05_only_numbers(self):
        with self.assertRaises(ValueError):
            strong_password('12345678')


    def test_05_ok(self):
        self.assertTrue(strong_password('Abcdefg0'))


if __name__ == "__main__":
    unittest.main()
