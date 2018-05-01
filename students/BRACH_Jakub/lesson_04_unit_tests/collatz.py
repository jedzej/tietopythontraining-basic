import unittest


class TestCollatzMethod(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            Collatz("aoeu")

    def test_for_8(self):
        self.assertEqual(Collatz(8), 4)

    def test_for_5(self):
        self.assertEqual(Collatz(5), 16)


# Collatz Sequemce
def Collatz(number):
    if number % 2 == 0:
        retval = number // 2
    else:
        retval = 3 * number + 1
    print(retval)
    return retval


if __name__ == '__main__':
    unittest.main()
