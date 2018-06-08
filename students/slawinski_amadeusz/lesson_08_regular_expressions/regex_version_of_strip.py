#!/usr/bin/env python3

import re
import unittest


def regex_strip(string, chars=" "):
    escapechars = re.escape(chars)
    regex = re.compile(r'^[' + escapechars + ']*(.*?)[' + escapechars + ']*$')
    match = regex.search(string)
    return match.group(1)


class RegexStripTest(unittest.TestCase):
    def testEmptyArg(self):
        result = regex_strip("  xx  ")
        self.assertEqual(result, "xx")
        result = regex_strip("  xxab")
        self.assertEqual(result, "xxab")
        result = regex_strip("abxx  ")
        self.assertEqual(result, "abxx")
        result = regex_strip("abxxab")
        self.assertEqual(result, "abxxab")

    def testOneChar(self):
        result = regex_strip("  xx  ", " ")
        self.assertEqual(result, "xx")
        result = regex_strip("abxxab", "a")
        self.assertEqual(result, "bxxab")
        result = regex_strip("abxxab", "b")
        self.assertEqual(result, "abxxa")

    def testTwoChars(self):
        result = regex_strip("  xx  ", "ab")
        self.assertEqual(result, "  xx  ")
        result = regex_strip("abxxab", "a")
        self.assertEqual(result, "bxxab")
        result = regex_strip("abxxab", "b")
        self.assertEqual(result, "abxxa")

    def testSpecialChars(self):
        result = regex_strip(" [xx] ", "[]")
        self.assertEqual(result, " [xx] ")
        result = regex_strip("[ xx ]", "[]")
        self.assertEqual(result, " xx ")
        result = regex_strip("\ xx /", "\/")
        self.assertEqual(result, " xx ")


if __name__ == '__main__':
    unittest.main()
