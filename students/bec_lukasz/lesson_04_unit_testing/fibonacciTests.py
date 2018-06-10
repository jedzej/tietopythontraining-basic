import unittest


def fib(number):

    if number is not int(number):
        raise ValueError
    elif number is None:
        raise TypeError
    elif number <= 0:
        raise RecursionError
    else:
        if number == 1 or number == 2:
            return 1
        else:
            return fib(number - 1) + fib(number - 2)


class FibonacciTests(unittest.TestCase):

    def test_if_number_1_is_equal_1(self):
        number = 1
        self.assertEqual(fib(number), 1)

    def test_if__number_2_is_equal_1(self):
        number = 2
        self.assertEqual(fib(number), 1)

    def test_if__number_6_is_equal_8(self):
        number = 6
        self.assertEqual(fib(number), 8)

    def test_if_zero_returns_recursion_error(self):
        number = 0
        self.assertRaises(RecursionError, fib, number)

    def test_if_negative_number_returns_recursion_error(self):
        number = -1
        self.assertRaises(RecursionError, fib, number)

    def test_float_number_returns_value_error(self):
        number = 1.0
        self.assertRaises(ValueError, fib, number)

    def test_if_string_returns_value_error(self):
        number = 'string'
        self.assertRaises(ValueError, fib, number)

    def test_if_None_returns_type_error(self):
        number = None
        self.assertRaises(TypeError, fib, number)
