import unittest
from collatz_input_validation import collatz
#from lesson_03_functions.collatz_input_validation import collatz


class TestCollatzFunction(unittest.TestCase):
    def test_TypeError(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_value_eight(self):
        self.assertEqual(collatz(8), 4)

    def test_value_five(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
