import unittest


def collatz(number):
    if number < 0:
        raise ValueError("Not found")
    elif number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


class MyTest(unittest.TestCase):

    def test_type_error(self):
        self.assertRaises(TypeError, collatz, 'aoeu')


    def test_returns_4_from_8(self):
        self.assertEqual(collatz(8), 4)


    def test_returns_16_from_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
