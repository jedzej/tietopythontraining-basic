#!/usr/bin/env python3

import re
import unittest


def validate_email(email):
    regex = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    match = regex.search(email)
    if match is None:
        return False
    return True


class ValidateEmailTest(unittest.TestCase):
    def testValidEmails(self):
        email = '''abc@example.com'''
        result = validate_email(email)
        self.assertTrue(result)

    def testInvalidEmails(self):
        email = '''abc.example.com'''
        result = validate_email(email)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
