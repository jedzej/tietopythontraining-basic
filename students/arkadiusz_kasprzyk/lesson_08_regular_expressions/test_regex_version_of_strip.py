import unittest

from regex_version_of_strip import *


class TestRegexStrip(unittest.TestCase):


    def test_01_space(self):
        self.assertEqual(regex_strip('  qq ryq   '), 'qq ryq')


    def test_02(self):
        self.assertEqual(regex_strip('qq ryq na patyq', 'yq'), ' ryq na pat')


    def test_03(self):
        self.assertEqual(regex_strip('qq ryq na patyq', 'yqr'), ' ryq na pat')


    def test_04(self):
        self.assertEqual(regex_strip('qq ryq na patyq', 'yqr '), 'na pat')


if __name__ == '__main__':
    unittest.main()
