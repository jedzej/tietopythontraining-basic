import unittest


def collatz(number):
    if number % 2 == 0:
        value = number // 2
    else:
        value = 3 * number + 1
    return value


class TestCollatzFunction(unittest.TestCase):
    def test_collatz_string(self):
        self.assertRaises(TypeError, collatz, 'aeou')

    def test_collatz_of_number_8(self):
        self.assertEqual(collatz(8), 4)

    def test_collatz_of_number_16(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
