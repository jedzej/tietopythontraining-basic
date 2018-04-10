import unittest


def collatz(number):
    if number == 0:
        return 1
    elif number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


class MyTest(unittest.TestCase):

    def test_collatz_aoeu(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_collatz_8(self):
        self.assertEqual(collatz(8), 4)

    def test_collatz_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
