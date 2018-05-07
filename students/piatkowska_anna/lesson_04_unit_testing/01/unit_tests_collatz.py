'''
Using unittest.TestCase write 4 unit tests for collatz() function
(not the whole script, just the function). Base on 26.4.1.
Basic example. Don't focus too much on class keyword in test definition.
Treat this as a code that must be there for tests to be ran.
Implement following tests:

Test that the function raises TypeError, if called on 'aoeu'
(use self.assertRaises),
Test that it returns 4, if called on 8,
Test that it returns 16, if called on 5.
Run the tests and fix the bugs, if any of the tests are failing.
'''
import unittest
import collatz


class CollatzTest(unittest.TestCase):

    def test_type_error_raised_when_aoeu_is_on_input(self):
        with self.assertRaises(TypeError):
            collatz.collatz('aoeu')

    def test_returns_4_when_called_on_8(self):
        self.assertEqual(collatz.collatz(8), 4)

    def test_returns_16_when_called_on_5(self):
        self.assertEqual(collatz.collatz(5), 16)


if __name__ == "__main__":
    unittest.main()
