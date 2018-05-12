#Using unittest.TestCase write 3 unit tests for collatz() function (not the whole script, just the function). Base on 26.4.1. Basic example. Don't focus too much on class keyword in test definition. Treat this as a code that must be there for tests to be ran. Implement following tests:
#
#    Test that the function raises TypeError, if called on 'aoeu' (use self.assertRaises),
#    Test that it returns 4, if called on 8,
#    Test that it returns 16, if called on 5.
#    Run the tests and fix the bugs, if any of the tests are failing.

import unittest

def collatz(number):
    ret = 0
    if (number%2 == 0):
        ret = number // 2
    else:
        ret = 3* number + 1

    print(ret)
    return ret

class TestCollatz(unittest.TestCase):

    def test_TypeError(self):
        self.assertRaises(TypeError, collatz, "aoeu")
    def test_8(self):
        self.assertEqual(collatz(8), 4)
    def test_5(self):
        self.assertEqual(collatz(5), 16)


if __name__ == '__main__':
    unittest.main()
