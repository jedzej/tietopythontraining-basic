import unittest


def collatz(x):
    if x % 2 == 0:
        res = x // 2
    else:
        res = 3 * x + 1
    # print(res)
    return res


class TestCollatzFunction(unittest.TestCase):

    def test_return4_if_called8(self):
        self.assertEqual(collatz(8), 4)

    def test_return16_if_called5(self):
        self.assertEqual(collatz(5), 16)

    def test_raises_type_error(self):
        s = 'aeou'
        with self.assertRaises(TypeError):
            collatz(s)


if __name__ == '__main__':
    unittest.main()