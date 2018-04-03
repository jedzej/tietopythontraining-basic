import unittest
import sys
sys.path.insert(0, '../lesson_03_funtions/')
from fibonacci_numbers import fib


class MyUnitTest(unittest.TestCase):

    def test_assertRaises(self):
        self.assertRaises(fib('aoeu'))

    def test_output_validation_for_8(self):
        self.assertTrue(fib(8) == 21)

    def test_output_validation_for_20(self):
        self.assertTrue(fib(20) == 6765)


if __name__ == '__main__':
    unittest.main()
