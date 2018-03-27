import unittest
from Collatz_Sequence import collatz

class CollatzTest(unittest.TestCase):

    def test_1_TypeError(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_2_value_8(self):
        self.assertEqual(collatz(8), 4)

    def test_3_value_5(self):
        self.assertEqual(collatz(5), 16)

if __name__ == '__main__':
    unittest.main()
