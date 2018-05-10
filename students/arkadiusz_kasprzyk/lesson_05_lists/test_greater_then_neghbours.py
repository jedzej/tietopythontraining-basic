import pytest
import unittest
from greater_then_neighbours import *

class TestGreaterThenNeighbours(unittest.TestCase):

    def test_gtn_value(self):
        with self.assertRaises(TypeError):
            gtn(None)

    def test_gtn_012(self):
        self.assertEqual(gtn([]), 0, "!0")
        self.assertEqual(gtn([1]), 0, "!1")
        self.assertEqual(gtn([1, 1]), 0, "!2")

    def test_gtn_smaple(self):
        self.assertEqual(gtn([1, 4, 6, 3, 8, 6, 9, 0, 3, 5, 4, 6, 7, 4]), 5, "!!!")
