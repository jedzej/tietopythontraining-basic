import unittest
import collatz_sequence


class CollatzTest(unittest.TestCase):

    def test_type_error_raised_when_aoeu_is_on_input(self):
        with self.assertRaises(TypeError):
            collatz_sequence.collatz('aoeu')

    def test_returns_4_when_called_on_8(self):
        self.assertEqual(collatz_sequence.collatz(8), 4)

    def test_returns_16_when_called_on_5(self):
        self.assertEqual(collatz_sequence.collatz(5), 16)


if __name__ == "__main__":
    unittest.main()
