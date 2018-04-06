import unittest


class TestCollatz(unittest.TestCase):
    def test_TypeError_when_input_is_string(self):
        with self.assertRaises(TypeError):
            collatz('aoeu')

    def test_input_8_return_4(self):
        self.assertEqual(4, collatz(8))

    def test_input_5_return_16(self):
        self.assertEqual(16, collatz(5))


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
