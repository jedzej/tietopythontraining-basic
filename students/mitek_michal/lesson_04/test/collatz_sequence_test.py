import unittest

from lesson_04.src.collatz_sequence import collatz


class TestCollatzSequence(unittest.TestCase):

    def test_if_collatz_sequence_raises_type_error_when_string_provided(
            self):
        self.assertRaises(TypeError, collatz('aoeu'))

    def test_if_collatz_sequence_returns_4_when_8_provided(self):
        self.assertEqual(4, collatz(8))

    def test_if_collatz_sequence_returns_16_when_5_provided(self):
        self.assertEqual(16, collatz(5))
