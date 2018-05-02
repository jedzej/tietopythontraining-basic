import unittest

"Unit Under Test"


def collatz_calculation(value):
    if value == 1:
        return 1
    elif value % 2 == 0:
        return value >> 1
    elif value % 2 == 1:
        return 3 * value + 1


class CollatzTests(unittest.TestCase):

    """Test that the function raises TypeError, if called on 'aoeu'"""
    def test_string_to_collatz(self):
        self.assertRaises(TypeError, collatz_calculation, 'aoeu')

    """Test that it returns 4, if called on 8"""
    def test_8_to_collatz(self):
        self.assertEqual(collatz_calculation(8), 4)

    """Test that it returns 16, if called on 5"""
    def test_5_to_collatz(self):
        self.assertEqual(collatz_calculation(5), 16)


if __name__ == '__main__':
    unittest.main()
