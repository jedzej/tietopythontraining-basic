import unittest

from valid_email import *


class TestValidEmail(unittest.TestCase):


    def test_00_too_short(self):
        with self.assertRaises(ValueError):
            valid_email('a@b')


    def test_01_the_shortest(self):
        self.assertTrue(valid_email('a@b.c'))


    def test_02_little_longer_1(self):
        self.assertTrue(valid_email('a.b@c.d'))


    def test_03_using_dash(self):
        self.assertTrue(valid_email('a-b@c.d'))


    def test_04_dot_domain(self):
        with self.assertRaises(ValueError):
            valid_email('ab@.d')


    def test_05_name_dot(self):
        with self.assertRaises(ValueError):
            valid_email('a.@cd')


    def test_06_dash_and_dot(self):
        self.assertTrue(valid_email('a-b@c-d.e'))


    def test_07_dashes_and_dots(self):
        self.assertTrue(valid_email('a-b.0.1-2@c-d.34.5-6.e'))


if __name__ == "__main__":
    unittest.main()
