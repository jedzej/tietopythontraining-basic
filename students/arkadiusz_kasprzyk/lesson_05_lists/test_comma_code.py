import unittest
from comma_code import *

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']

class TestCommaCode(unittest.TestCase):

    def test_type_0(self):
        with self.assertRaises(TypeError):
            comma_code(None)

    def test_type_1(self):
        with self.assertRaises(TypeError):
            comma_code(123)

    def test_type_2(self):
        self.assertEqual(comma_code(list(range(3))), '0, 1 and 2', "int !-> str")

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


# if __name__ == '__main__':

#    unittest.main()
