import unittest
from fibonacci_numbers import fib


class TestFib(unittest.TestCase):

    def test_0(self):
        self.assertRaises(TypeError, fib, 'aoeu')

    def test_1(self):
        self.assertEqual(fib(8), 21)

    def test_2(self):
        self.assertEqual(fib(16), 987)


if __name__ == "__main__":
    unittest.main()
