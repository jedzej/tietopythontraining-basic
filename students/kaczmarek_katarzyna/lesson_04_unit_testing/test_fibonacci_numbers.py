import unittest
from fibonacci_numbers import fib


class TestFibMethod(unittest.TestCase):

    def test_value_error_on_negative_input_10(self):
        self.assertRaises(ValueError, fib, -10)

    def test_value_error_on_input_0(self):
        self.assertRaises(ValueError, fib, 0)

    def test_input_1(self):
        self.assertEqual(fib(1), 1)

    def test_input_2(self):
        self.assertEqual(fib(2), 1)

    def test_input_15(self):
        self.assertEqual(fib(15), 610)

    def test_recursion_error_on_input_5000(self):
        self.assertRaises(RecursionError, fib, 5000)

    def test_type_error_on_string(self):
        self.assertRaises(TypeError, fib, 'aoeu')

    def test_type_error_on_bool(self):
        self.assertRaises(TypeError, fib, True)

    def test_type_error_on_none(self):
        self.assertRaises(TypeError, fib, None)


if __name__ == '__main__':
    unittest.main()
