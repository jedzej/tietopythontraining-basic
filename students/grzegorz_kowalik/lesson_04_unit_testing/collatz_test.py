
import unittest
from students.grzegorz_kowalik.lesson_03_functions import collatz


class TestCollatz(unittest.TestCase):

    def test_type_error(self):
        with self.assertRaises(TypeError):
            collatz.collatz('aoeu')

    def test_correct_8(self):
        self.assertEqual(4, collatz.collatz(8))

    def test_correct_5(self):
        self.assertEqual(16, collatz.collatz(5))
