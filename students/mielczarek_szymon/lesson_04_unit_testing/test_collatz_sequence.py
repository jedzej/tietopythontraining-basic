import sys
import unittest
sys.path.append('..')
from lesson_03_functions.the_collatz_sequence import collatz


class TestCollatz(unittest.TestCase):
    def test_non_integer(self):
        with self.assertRaises(TypeError):
            collatz('aoeu')

    def test_value_8(self):
        self.assertEqual(collatz(8), 4)

    def test_value_5(self):
        self.assertEqual(collatz(5), 16)

    def test_negative_value(self):
        self.assertRaises(ValueError, collatz, -10)


if __name__ == '__main__':
    unittest.main()
