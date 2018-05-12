import unittest
from lesson_03.fibonacci_numbers import fib


class MyTest(unittest.TestCase):

    def test_1(self):
        self.assertRaises(TypeError, fib, None)

    def test_2(self):
        self.assertRaises(TypeError, fib, 'aoeu')

    def test_3(self):
        with self.assertRaises(RecursionError):
            fib(0)

    def test_4(self):
        self.assertEqual(fib(7), 13)


if __name__ == '__main__':
    unittest.main()
