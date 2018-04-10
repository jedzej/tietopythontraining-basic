import unittest
from collatz_sequence import collatz


class TestCollatzFunction(unittest.TestCase):

    def test8(self):
        self.assertEqual(collatz(8), 4, "problem with 8")

    def test16(self):
        self.assertEqual(collatz(16), 8, "problem with 16")

    def test_input(self):
        with self.assertRaises(TypeError):
            collatz('aoeu')


if __name__ == '__main__':
    unittest.main()
