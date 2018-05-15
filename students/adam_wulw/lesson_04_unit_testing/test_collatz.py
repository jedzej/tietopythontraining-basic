import unittest
from collatz import collatz


class TestStringMethods(unittest.TestCase):

    def test_collatz_1(self):
        with self.assertRaises(TypeError):
            collatz('aoue')

    def test_collatz_2(self):
        self.assertEqual(collatz(8), 4)

    def test_collatz_3(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
