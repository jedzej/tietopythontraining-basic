#!/usr/bin/env python3

import re
import unittest


def validate_phone_number(phone):
    regex = re.compile(r'''^
        (
        ([+]\d{2})              # country prefix part
        (
        \s\d{3}\s\d{3}\s\d{3}   # "+00 123 456 789"
        |                       # or
        \d{9}                   # "+00123456789"
        |                       # or
        \s\d{3}-\d{3}-\d{3}     # "+00 123-456-789"
        )
        |
        (
        \d{3}\s\d{3}\s\d{3}     # "123 456 789"
        |                       # or
        \d{9}                   # "123456789"
        |                       # or
        \d{3}-\d{3}-\d{3}       # "123-456-789"
        )
        )
        $''', re.VERBOSE)
    match = regex.search(phone)
    if match is None:
        return False
    return True


class ValidatePhoneNumberTest(unittest.TestCase):
    def testValidPhoneNumber(self):
        phone_number = '''123456789'''
        result = validate_phone_number(phone_number)
        self.assertTrue(result)
        phone_number = '''123 456 789'''
        result = validate_phone_number(phone_number)
        self.assertTrue(result)
        phone_number = '''123-456-789'''
        result = validate_phone_number(phone_number)
        self.assertTrue(result)
        phone_number = '''+00 123 456 789'''
        result = validate_phone_number(phone_number)
        self.assertTrue(result)
        phone_number = '''+00123456789'''
        result = validate_phone_number(phone_number)
        self.assertTrue(result)
        phone_number = '''+00 123-456-789'''
        result = validate_phone_number(phone_number)
        self.assertTrue(result)

    def testInvalidPhoneNunberTest(self):
        phone_number = '''12 3456789'''
        result = validate_phone_number(phone_number)
        self.assertFalse(result)
        phone_number = '''123-456 789'''
        result = validate_phone_number(phone_number)
        self.assertFalse(result)
        phone_number = '''123 456-789'''
        result = validate_phone_number(phone_number)
        self.assertFalse(result)
        phone_number = '''+00-123-456-789'''
        result = validate_phone_number(phone_number)
        self.assertFalse(result)
        phone_number = '''+00123 456 789'''
        result = validate_phone_number(phone_number)
        self.assertFalse(result)
        phone_number = '''+00 123456 789'''
        result = validate_phone_number(phone_number)
        self.assertFalse(result)
        phone_number = '''+00 123 456789'''
        result = validate_phone_number(phone_number)
        self.assertFalse(result)
        phone_number = '''00123456789'''
        result = validate_phone_number(phone_number)
        self.assertFalse(result)
        pass


if __name__ == '__main__':
    unittest.main()
