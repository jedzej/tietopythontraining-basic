import unittest


# Function under test
def collatz(number):
    if number % 2 == 0:
        result = (number // 2)
    else:
        result = 3 * number + 1
    print(result)
    return result


class TestCollatzSequence(unittest.TestCase):

    def test_collatz_type_error(self):
        self.assertRaises(TypeError, collatz, 'aoue')

    def test_collatz_input_8(self):
        self.assertEqual(collatz(8), 4)

    def test_collatz_input_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
