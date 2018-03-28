import unittest


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result


class TestCollatzMethod(unittest.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError):
            collatz('aoeu')

    def test_even(self):
        self.assertEqual(collatz(8), 4)

    def test_odd(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
