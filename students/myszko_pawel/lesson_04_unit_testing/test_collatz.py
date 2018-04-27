import unittest
from collatz import collatz

class TestCollatzFunction(unittest.TestCase):

    def test_type_error(self):
        with self.assertRaises(TypeError):
            collatz('aoeu')

    def test_8(self):
        self.assertEqual(collatz(8), 4)

    def test_5(self):
        self.assertEqual(collatz(5), 16)

if __name__ == '__main__':
    unittest.main()
