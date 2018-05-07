import unittest
import fibonacci_number


class FibonacciTest(unittest.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci_number.fib('aoeu')

    def test_type_none(self):
        with self.assertRaises(TypeError):
            fibonacci_number.fib(None)

    def test_negative_value(self):
        with self.assertRaises(RecursionError):
            fibonacci_number.fib(-5)

    def test_give_6_return_8(self):
        self.assertEquals(fibonacci_number.fib(6), 8)

    def test_one(self):
        self.assertEquals(fibonacci_number.fib(1), 1)


if __name__ == "__main__":
    unittest.main()
