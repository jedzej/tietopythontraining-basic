import unittest
import re


def validate_email(email):
    rgx_email = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[A-Za-z0-9]+(\.[a-zA-Z]{2,4})$')
    matched_object = rgx_email.search(email)
    if matched_object is not None:
        print("Valid")
    else:
        print("Email is not valid")
    return matched_object


if __name__ == '__main__':
    email = input("Enter email: ")
    validate_email(email)


class TestsValidateEmail(unittest.TestCase):

    def test_simple_mail(self):
        self.assertNotEqual(validate_email("valid@email.com"), None)

    def test_long_mail(self):
        self.assertNotEqual(validate_email(
            "12eff567ddsdsdvalid@extralongdomain1233.com"), None)

    def test_prefix_suffix(self):
        self.assertEqual(validate_email("####valid@email.com###"), None)

    def test_suffix(self):
        self.assertEqual(validate_email("valid@email.com####1!)"), None)

    def test_prefix_with_space(self):
        self.assertEqual(validate_email("## valid@email.com"), None)

    def test_no_monkey(self):
        self.assertEqual(validate_email("valid$email.com"), None)

    def test_no_dot(self):
        self.assertEqual(validate_email("valid@email,com"), None)

    def test_empty_name(self):
        self.assertEqual(validate_email("@email,com"), None)
