import re
import unittest


def check_password(password):
    digits_rgx = re.compile(r'\d')
    case_rgx = re.compile(r'[A-Z]+')

    digits_ok = bool(digits_rgx.search(password))
    len_ok = len(password) >= 8
    case_ok = bool(case_rgx.search(password))
    conditions = digits_ok, len_ok, case_ok

    if all(conditions):
        print("Strong Password")
        return True
    else:
        print("Weak Password")
        return False


if __name__ == '__main__':
    password = input()
    check_password(password)


class TestsValidatePassword(unittest.TestCase):

    def test_only_one_digit(self):
        self.assertEqual(
            check_password("kleskap1"), False)

    def test_only_upper_case(self):
        self.assertEqual(
            check_password("kleskapR"), False)

    def test_len_lower(self):
        self.assertEqual(
            check_password("1Rabc$"), False)

    def test_one_digit_upper_case_len_min_eight(self):
        self.assertEqual(
            check_password("1Rabcsd#4sds"), True)

    def test_one_digit_upper_case_len_equal_eight(self):
        self.assertEqual(
            check_password("abcd3aBc"), True)
