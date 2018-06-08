#!/usr/bin/env python3

import unittest


def sum_all(*args):
    return sum(args)


class sum_allTest(unittest.TestCase):
    def testNoArgument(self):
        self.assertEqual(sum_all(), 0, "sum_all() != 0")

    def testOneArgument(self):
        self.assertEqual(sum_all(1), 1, "sum_all(1) != 1")
        self.assertEqual(sum_all(2), 2, "sum_all(2) != 2")

    def testTwoArguments(self):
        self.assertEqual(sum_all(1, 2), 3, "sum_all(1, 2) != 3")
        self.assertEqual(sum_all(2, 3), 5, "sum_all(2, 3) != 5")

    def testThreeArguments(self):
        self.assertEqual(sum_all(1, 2, 3), 6, "sum_all(1, 2, 3) != 6")
        self.assertEqual(sum_all(2, 3, 7), 12, "sum_all(2, 3, 7) != 12")

    def testTenArguments(self):
        self.assertEqual(sum_all(0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 45,
                         "sum_all(0, 1, 2, 3, 4, 5, 6, 7, 8, 9) != 45")


if __name__ == "__main__":
    unittest.main()
