import unittest

def fib(n):
    if n > 0:
        if n == 1 or n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        raise ValueError

class TestFib(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            fib('aoeu')

    def test_none(self):
        with self.assertRaises(TypeError):
            fib(None)

    def test_0(self):
        with self.assertRaises(ValueError):
            fib(0)

    def test_1(self):
        self.assertEqual(fib(1), 1, "fib(1) != 1")

    def test_2(self):
        self.assertEqual(fib(2), 1, "fib(2) != 1")

    def test_3(self):
        self.assertEqual(fib(3), 2, "fib(3) != 2")

    def test_4(self):
        self.assertEqual(fib(4), 3, "fib(4) != 3")

    def test_5(self):
        self.assertEqual(fib(5), 5, "fib(5) != 5")

    def test_6(self):
        self.assertEqual(fib(6), 8, "fib(6) != 8")


if __name__ == '__main__':
    unittest.main()