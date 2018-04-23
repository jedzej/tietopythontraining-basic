import unittest


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


class TestCollatz(unittest.TestCase):

    def test_if_function_raises_type_error(self):
        with self.assertRaises(TypeError):
            collatz('aeou')

    def test_if_function_returns_4_when_called_on_8(self):
        self.assertEqual(collatz(8), 4)

    def test_if_function_returns_16_when_called_on_5(self):
        self.assertEqual(collatz(5),16)


if __name__ == '__main__':
    unittest.main()
