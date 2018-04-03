# Tests for Collatz Sequence
import unittest
import collatz


class CollatzTest(unittest.TestCase):
    # Test that the function raises TypeError, if called on 'aoeu'
    def test_checkstring(self):
        self.assertRaises(TypeError, collatz.collatz('aoeu'))

    # Test that it returns 4, if called on 8,
    def test_checkvalue1(self):
        self.assertEqual(collatz.collatz(8),4)

    # Test that it returns 16, if called on 5.
    def test_checkvalue2(self):
        self.assertEqual(collatz.collatz(5),16)


if __name__ == '__main__':
    unittest.main()
