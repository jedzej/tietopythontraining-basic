import unittest

from lesson_03_functions.collatz import collatz


class TestCollatz(unittest.TestCase):

    def test_if_collatz_return_type_error(self):
        with self.assertRaises(TypeError):
            collatz('aeou')

    def test_if_collatz_return_4_when_arg_is_8(self):
        self.assertEqual(collatz(8), 4)

    def test_if_collatz_return_16_when_arg_is_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
