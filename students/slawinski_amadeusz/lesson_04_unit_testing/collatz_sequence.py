#!/usr/bin/env python3

import unittest


def collatz(number):
    if number % 2:
        ret = 3 * number + 1
    else:
        ret = number // 2
    return ret


class CollatzTest(unittest.TestCase):
    def testTypeError(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def testReturn4for8(self):
        self.assertEqual(collatz(8), 4, "collatz(8) != 4")

    def testReturn16for5(self):
        self.assertEqual(collatz(5), 16, "collatz(5) != 16")


if __name__ == '__main__':
    unittest.main()
