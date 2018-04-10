import unittest
from comma_code import *

<<<<<<< HEAD
<<<<<<< HEAD
=======
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']

>>>>>>> 01 On branch adziu/lesson_05_lists
=======
>>>>>>> 02 adziu/lesson_05_lists
class TestCommaCode(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            comma_code(None)

<<<<<<< HEAD
<<<<<<< HEAD
    def test_type_2(self):
        self.assertEqual(comma_code(list(range(3))), '0, 1 and 2', "int !-> str")
=======
    def test_type(self):
        with self.assertRaises(TypeError):
            comma_code(123)
>>>>>>> 01 On branch adziu/lesson_05_lists
=======
    def test_type_2(self):
        self.assertEqual(comma_code(list(range(3))), '0, 1 and 2', "int !-> str")
>>>>>>> 02 adziu/lesson_05_lists

    def test_0(self):
        self.assertEqual(comma_code([]), '', "comma_code([]) != ''")

    def test_1(self):
        self.assertEqual(comma_code(['apples']), 'apples',
                         "comma_code(['apples']) != 'apples'")

    def test_2(self):
        self.assertEqual(comma_code(['apples', 'bananas']),
                         'apples and bananas',
                         "comma_code(['apples', 'bananas']) != 'apples and bananas'")

    def test_3(self):
        self.assertEqual(comma_code(['apples', 'bananas', 'tofu',]),
                         'apples, bananas and tofu',
                         "comma_code(['apples', 'bananas']) != 'apples, bananas and tofu'")

    def test_5(self):
        self.assertEqual(comma_code(['apples', 'bananas', 'tofu', 'cats', 'dogs']),
                         'apples, bananas, tofu, cats and dogs',
                         "Ooops...")


#if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< HEAD
#    unittest.main()

=======
#    unittest.main()
>>>>>>> 01 On branch adziu/lesson_05_lists
=======
#    unittest.main()

>>>>>>> 02 adziu/lesson_05_lists
