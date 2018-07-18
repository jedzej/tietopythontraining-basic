import re
import unittest


def validate_phone_nr(nr):
    regex = re.compile(r'(^\+\d{2})( |-)?(\d{3})( |-)?(\d{3})( |-)?(\d{3}$)')
    matched_object = regex.search(nr)
    if matched_object:
        print("Valid")
    else:
        print("Not Valid")
    return matched_object


if __name__ == '__main__':
    nr = input()
    validate_phone_nr(nr)


class TestsValidatePhone(unittest.TestCase):

    def test_mail_space(self):
        self.assertNotEqual(
            validate_phone_nr("+48 111 111 111"), None)

    def test_mail_dash(self):
        self.assertNotEqual(
            validate_phone_nr("+48-111-111-111"), None)

    def test_mail_no_space(self):
        self.assertNotEqual(
            validate_phone_nr("+48111111111"), None)

    def test_mail_char(self):
        self.assertEqual(
            validate_phone_nr("+48 999 111 22x"), None)

    def test_mail_missing_digit(self):
        self.assertEqual(
            validate_phone_nr("+48 999 111 22"), None)

    def test_mail_additional_space(self):
        self.assertEqual(validate_phone_nr
                         ("+48 +48 +11 +11 --- 111 ---111 ------111"), None)
