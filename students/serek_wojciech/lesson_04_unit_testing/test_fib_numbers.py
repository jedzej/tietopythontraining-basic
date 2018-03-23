"""Unit tests for fib function using unittest"""
import unittest
from lesson_03_functions.fibonacci_numbers import fib


class TestFibNumbers(unittest.TestCase):
    """Unit test class for collatz function"""

    def test_fib_none(self):
        """Test None as parameter"""
        self.assertRaises(TypeError, fib, 'aoeu')

    def test_fib_non_integer(self):
        """Test non integer as parameter"""
        self.assertRaises(TypeError, fib, 'aoeu')

    def test_fib_1(self):
        """Test 1 as parameter"""
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        """Test 2 as parameter"""
        self.assertEqual(fib(2), 1)

    def test_fib_3(self):
        """Test 3 as parameter"""
        self.assertEqual(fib(3), 2)

    def test_fib_4(self):
        """Test 4 as parameter"""
        self.assertEqual(fib(4), 3)

    def test_fib_5(self):
        """Test 5 as parameter"""
        self.assertEqual(fib(5), 5)

    def test_fib_6(self):
        """Test 6 as parameter"""
        self.assertEqual(fib(6), 8)

    def test_fib_7(self):
        """Test 7 as parameter"""
        self.assertEqual(fib(7), 13)

    def test_negative(self):
        """Test negative value as parameter"""
        try:
            fib(-1)
            self.fail("No exception raised")
        except RuntimeError as exception:
            self.assertEqual(str(exception), 'maximum recursion depth exceeded'
                                             ' in comparison')


if __name__ == '__main__':
    unittest.main()
