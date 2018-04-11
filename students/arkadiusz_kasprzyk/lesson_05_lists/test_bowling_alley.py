import unittest
from bowling_alley import *

class TestBowling(unittest.TestCase):

    def test_bowling_type_1(self):
        with self.assertRaises(TypeError):
            bowling(None, [[1, 2]])

    def test_bowling_type_2(self):
        with self.assertRaises(TypeError):
            bowling(5, None)

    def test_bowling_value_1(self):
        with self.assertRaises(ValueError):
            bowling(-1, [[1, 2]])

    def test_bowling_value_2(self):
        with self.assertRaises(ValueError):
            bowling(1, [[1]])

    def test_bowlig_0_1(self):
        self.assertEqual(bowling(0, [[1, 2]]), [], "1: !0")

    def test_bowlig_0_2(self):
        self.assertEqual(bowling(3, []), ['I', 'I', 'I'], "2: !all")

    def test_bowlig_sample(self):
        self.assertEqual(bowling(5, [[1, 2], [4, 5]]), ['.', '.', 'I', '.', '.'], "3: !all")