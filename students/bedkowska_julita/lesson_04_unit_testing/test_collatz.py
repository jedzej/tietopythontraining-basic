import unittest
from students.bedkowska_julita.lesson_03_functions.the_collatz_sequence \
    import collatz


class TestCollatz(unittest.TestCase):

    def test_TypeError(self):
        self.assertRaises(TypeError, collatz, 'aoeu')

    def test_4(self):
        self.assertEqual(collatz(8), 4)

    def test_16(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
