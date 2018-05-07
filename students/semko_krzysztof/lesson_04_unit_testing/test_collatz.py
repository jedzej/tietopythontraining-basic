import unittest

from the_collatz_sequence import collatz


class TestCollatzFunction(unittest.TestCase):
    def testTypeError(self):
        with self.assertRaises(TypeError):
            collatz('aeou')

    def testValue_8(self):
        self.assertEqual(collatz(8), 4)

    def testValue_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
