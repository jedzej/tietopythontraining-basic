import unittest
from lesson_03_functions.the_collatz_sequence import collatz


class TestCollatzFunction(unittest.TestCase):
    def test_invalid_type(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_value_8(self):
        self.assertEqual(collatz(8), 4)

    def test_value_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
