import unittest

from fibonacci_numbers import fib


class TestFibonacciNumbers(unittest.TestCase):
    def testNoneValue(self):
        with self.assertRaises(TypeError):
            fib(None)

    def testStringValue(self):
        with self.assertRaises(TypeError):
            fib("aeou")

    def testSequenceNumber8(self):
        self.assertEqual(fib(8), 21)

    def testSequenceNumber16(self):
        self.assertEqual(fib(16), 987)


if __name__ == '__main__':
    unittest.main()
