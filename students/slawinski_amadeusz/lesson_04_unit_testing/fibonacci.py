#!/usr/bin/env python3

import unittest


def fib(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError
    elif int(n) == 0:
        return 0
    elif int(n) == 1:
        return 1
    else:
        return fib(int(n) - 1) + fib(int(n) - 2)


class TestFibonacci(unittest.TestCase):
    def testTypeError_for_None(self):
        self.assertRaises(ValueError, fib, None)

    def testValueError_for_string(self):
        self.assertRaises(ValueError, fib, "string")

    def testValueError_for_float(self):
        self.assertRaises(ValueError, fib, 1.11)

    def testNegativeValue(self):
        self.assertRaises(ValueError, fib, -1)
        self.assertRaises(ValueError, fib, -100)

    def testResultFor0(self):
        self.assertEqual(fib(0), 0, "fib(0) != 0")

    def testResultFor1(self):
        self.assertEqual(fib(1), 1, "fib(1) != 1")

    def testResultFor2(self):
        self.assertEqual(fib(2), 1, "fib(2) != 1")

    def testResultFor3(self):
        self.assertEqual(fib(3), 2, "fib(3) != 2")

    def testResultFor10(self):
        self.assertEqual(fib(10), 55, "fib(10) != 55")

    def testResultFor20(self):
        self.assertEqual(fib(20), 6765, "fib(20) != 6765")


if __name__ == '__main__':
    unittest.main()
