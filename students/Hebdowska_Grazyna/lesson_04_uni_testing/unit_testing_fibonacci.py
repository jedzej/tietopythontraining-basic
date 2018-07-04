import unittest


def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)


class MyTest(unittest.TestCase):

    def test_fibonaci_none(self):
        self.assertRaises(TypeError, fib, None)

    def test_fib_aoeu(self):
        self.assertRaises(TypeError, fib, 'aoeu')

    def test_fib_0(self):
        self.assertEqual(fib(0), 0)

    def test_fib_3(self):
        self.assertEqual(fib(3), 2)

    def test_fib_11(self):
        self.assertEqual(fib(11), 89)


if __name__ == '__main__':
    unittest.main()
