import unittest
from lesson_03_functions.the_collatz_sequence_and_input_validation \
    import collatz


class MyTest(unittest.TestCase):
    def test_type_error(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_returns_4_if_called_on_8(self):
        self.assertEqual(collatz(8), 4)

    def test_returns_16_if_called_on_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == "__main__":
    unittest.main()
