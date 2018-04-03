import unittest
import sys
sys.path.insert(0, '../lesson_03_funtions/')
from the_collatz_sequence import collatz


class MyFirstUnitTest(unittest.TestCase):

    def test_assertRaises(self):
        self.assertRaises(collatz('aoeu'))

    def test_output_validation_for_8(self):
        self.assertTrue(collatz(8) == 4)

    def test_output_validation_for_5(self):
        self.assertTrue(collatz(5) == 16)


if __name__ == '__main__':
    unittest.main()
