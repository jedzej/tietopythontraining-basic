import unittest
import Collatz


class TestCollatzFunction(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            Collatz.get_collatz_nr("aeou")

    def test_expected_collatz_nr(self):
        self.assertEqual(Collatz.get_collatz_nr(8), 4, "Collatz function returned unexpected value")
        self.assertEqual(Collatz.get_collatz_nr(5), 16, "Collatz function returned unexpected value")
        self.assertNotEqual(Collatz.get_collatz_nr(123), 371, "Collatz function returned unexpected value")


if __name__ == '__main__':
    unittest.main()
