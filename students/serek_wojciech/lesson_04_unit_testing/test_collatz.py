"""Unit tests for collatz function using unittest"""
import unittest
from lesson_03_functions.collatz_and_input_validation import collatz


class TestCollatz(unittest.TestCase):
    """Unit test class for collatz function"""

    def test_none_integer(self):
        """Test non integer value as parameter"""
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_4(self):
        """Test return value 4"""
        self.assertEqual(collatz(8), 4)

    def test_16(self):
        """Test return value 16"""
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
