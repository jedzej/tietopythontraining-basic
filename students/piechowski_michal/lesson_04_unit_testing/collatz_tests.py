#!/usr/bin/env python3

import unittest
from students.piechowski_michal.lesson_03_functions.collatz_sequence import collatz


class CollatzTest(unittest.TestCase):

    def test_collatz_raises_type_error_with_invalid_input(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_collatz_returns_correct_value(self):
        self.assertEqual(collatz(8), 4)
        self.assertEqual(collatz(5), 16)

    def test_collatz_raises_value_error_with_negative_input(self):
        self.assertRaises(ValueError, collatz, -1)


if __name__ == "__main__":
    unittest.main()
