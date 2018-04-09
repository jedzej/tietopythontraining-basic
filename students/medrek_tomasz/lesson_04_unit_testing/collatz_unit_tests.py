#!/usr/bin/env python3


import unittest
from the_collatz_sequence import collatz


class CollatzUnitTests(unittest.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError):
            collatz('aoeu')

    def test_return_value_1(self):
        self.assertEqual(collatz(8), 4)

    def test_return_value_2(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
