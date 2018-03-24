import unittest


# Function under test
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


class TestFibonacciNumbers(unittest.TestCase):

    def test_fib_type_error(self):
        self.assertRaises(TypeError, fib, 'aoue')

    def test_fib_input_5(self):
        self.assertEqual(fib(5), 5)

    def test_fib_input_12(self):
        self.assertEqual(fib(12), 144)


if __name__ == '__main__':
    unittest.main()
