import unittest


def collatz(number):

    try:

        if number % 2 == 0:
            print(number // 2)
            return number // 2
        elif number % 2 == 1:
            print(3 * number + 1)
            return 3 * number + 1

    except TypeError:
        print('Only digits accepted')


class CollatzTests(unittest.TestCase):

    def test_type_error(self):
        self.assertRaises(TypeError, collatz('aoeu'))

    def test_return_4_if_8_called(self):
        self.assertTrue(collatz(8), 4)

    def test_return_16_if_5_called(self):
        self.assertTrue(collatz(5), 16)
