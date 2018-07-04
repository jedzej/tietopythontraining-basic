import unittest


def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


class TestFibbonacci(unittest.TestCase):

    def test_return5_if_called5(self):
        self.assertEqual(fib(5), 5)

    def test_return610_if_called15(self):
        self.assertEqual(fib(5), 5)

    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            fib('aeou')

    def test_non_value(self):
        with self.assertRaises(TypeError):
            fib('None')

    def test_negative_value(self):
        with self.assertRaises(RecursionError):
            fib(-1)


if __name__ == "__main__":
    unittest.main()