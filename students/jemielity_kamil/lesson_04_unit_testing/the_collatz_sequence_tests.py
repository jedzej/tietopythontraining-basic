import unittest

from students.jemielity_kamil.lesson_03_functions.the_collatz_sequence import collatz


class MyTest(unittest.TestCase):

    def test_collatz_string_value(self):
        self.assertRaises(TypeError, collatz, 'aeou')

    def test_collatz_of_number_8(self):
        self.assertEqual(collatz(8), 4, 'Colltaz of number 8 != 4')

    def test_collatz_of_number_16(self):
        self.assertEqual(collatz(5), 16, 'Colltaz of number 5 != 16')


if __name__ == '__main__':
    unittest.main()
