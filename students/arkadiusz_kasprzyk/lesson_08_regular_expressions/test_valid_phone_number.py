import unittest

from valid_phone_number import *


class TestValidPhoneNumber(unittest.TestCase):


    def test_wrong_01(self):
        with self.assertRaises(ValueError):
            valid_phone_number('+48 123 456')


    def test_wrong_02(self):
        with self.assertRaises ( ValueError ):
            valid_phone_number('23 456 789')


    def test_wrong_03(self):
        with self.assertRaises(ValueError):
            valid_phone_number('3 456 789')


    def test_wrong_04(self):
        with self.assertRaises(ValueError):
            valid_phone_number('0123 456 789')


    def test_ok_01(self):
        self.assertTrue(valid_phone_number('123-456-789'))


    def test_ok_02(self):
        self.assertTrue(valid_phone_number('+48 123-456-789'))


    def test_ok_03(self):
            self.assertTrue(valid_phone_number('0048 123-456-789'))


    def test_ok_04(self):
        self.assertTrue(valid_phone_number('123 456 789'))


    def test_ok_05(self):
        self.assertTrue (valid_phone_number('+48 123 456 789'))


    def test_ok_06(self):
        self.assertTrue (valid_phone_number('+48 123-456 789'))
        # OK, but should it be OK?


if __name__ == "__main__":
    unittest.main()
