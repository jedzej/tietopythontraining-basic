import unittest
from fibonacci_numbers import fib


class TestFib(unittest.TestCase):

    def test_0(self):
        self.assertRaises(fib(aoeu))

    def test_1(self):
        self.assertRaises(fib(8), 4)

    def test_2(self):
        self.assertRaises(fib(16), 5)


if __name__ == "__main__":
    unittest.main()
