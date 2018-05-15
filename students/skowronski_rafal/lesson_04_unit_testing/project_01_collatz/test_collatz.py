import unittest
from collatz import collatz


class TestCollatz(unittest.TestCase):
    def test_collatz_on_aoeu_raises_type_error(self):
        with self.assertRaises(TypeError):
            collatz('aoeu')

    def test_collatz_on_eight_returns_four(self):
        self.assertEqual(collatz(8), 4)

    def test_collatz_on_five_returns_sixteen(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main(verbosity=2)
