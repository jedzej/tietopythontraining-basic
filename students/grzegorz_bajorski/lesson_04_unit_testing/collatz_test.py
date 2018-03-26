import unittest
from the_collatz_seq import collatz

class MyTests(unittest.TestCase):

    def test_1(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_2(self):
        self.assertEqual(collatz(8), 4)

    def test_3(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
