import unittest
from the_collatz_sequence_and_validation import collatz


class TestFunctionCollatz(unittest.TestCase):
    def test_type_error(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_argument_eight(self):
        self.assertEqual(collatz(8), 4)

    def test_argument_five(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
