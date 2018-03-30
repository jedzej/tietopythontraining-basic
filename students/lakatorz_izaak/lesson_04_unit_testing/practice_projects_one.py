# Using unittest.TestCase write 3 unit tests for collatz() function (not the
#  whole script, just the function). Base on 26.4.1. Basic example. Don't
# focus too much on class keyword in test definition. Treat this as a code
# that must be there for tests to be ran. Implement following tests:

import unittest
import the_collatz_sequence


class TestStringMethods(unittest.TestCase):

    def test_if_raises_typeError(self):
        self.assertRaises(TypeError, the_collatz_sequence.collatz, 'aoeu')

    def test_if_returns_four(self):
        self.assertEqual(the_collatz_sequence.collatz(8), 4)

    def test_if_returns_sixteen(self):
        self.assertEqual(the_collatz_sequence.collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
