import unittest
from swap_min_and_max import swap_min_max as smm

class TestSwapMinMax(unittest.TestCase):

    def test_smm_type(self):
        with self.assertRaises(TypeError):
            smm(None)

    def test_smm_01(self):
        self.assertEqual(smm([]), [], "!0")
        self.assertEqual(smm([1]), [1], "!1")

    def test_smm_02(self):
        self.assertEqual(smm([0,1]), [1, 0], "!2")

    def test_smm_sample(self):
        self.assertEqual(smm( [3, 0, 1, 4, 7, 2, 6]),  [3, 7, 1, 4, 0, 2, 6], "!sample")

    def test_smm_ambig_min(self):
        self.assertEqual(smm( [3, 0, 0, 4, 7, 2, 6]),  [3, 7, 0, 4, 0, 2, 6], "!ambig_min")

    def test_smm_ambig_max(self):
        self.assertEqual(smm( [3, 0, 1, 4, 7, 7, 6]),  [3, 7, 1, 4, 0, 7, 6], "!ambig_min")