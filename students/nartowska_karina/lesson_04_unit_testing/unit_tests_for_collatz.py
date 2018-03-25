import unittest


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def input_collatz():
    print("Type an positive integer: ")
    number = int(input())
    while number != 1:
        number = collatz(number)
        print(number)


def main():
    try:
        input_collatz()
    except ValueError:
        print("Value must be an integer")


class MyTest(unittest.TestCase):
    def test_type_error(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_returns_4_if_called_on_8(self):
        self.assertEqual(collatz(8), 4)

    def test_returns_16_if_called_on_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == "__main__":
    unittest.main()
