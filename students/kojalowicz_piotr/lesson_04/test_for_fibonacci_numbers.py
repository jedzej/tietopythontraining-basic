import math
import unittest


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_with_input(n):
    correct_input = None
    while correct_input is None:
        try:
            if n >= 0:
                correct_input = 1
                return fib(n)
            else:
                print('The number must integer biger then -1')
                n = int(input())
        except ValueError:
            print('The number must integer biger then -1')
            n = int(input())


class MyTest(unittest.TestCase):
    def test0(self):
        self.assertRaises(TypeError, fib, None)

    def test1(self):
        self.assertEqual(fib(2), 1)

    def test3(self):
        self.assertEqual(fib_with_input(-3), 1)


if __name__ == '__main__':
    unittest.main()
