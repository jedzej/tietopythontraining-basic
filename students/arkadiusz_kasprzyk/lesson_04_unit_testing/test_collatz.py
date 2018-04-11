import unittest


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


class TestCollatz(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            collatz('aoeu')

    def test_8_4(self):
        self.assertEqual(collatz(8), 4, "collatz(8) != 4")

    def test_5_16(self):
        self.assertEqual(collatz(5), 16, "collatz(5) != 16")


if __name__ == '__main__':
    unittest.main()

