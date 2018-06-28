#!/usr/bin/env python3

import re
import unittest


def validate_postal_code(code):
    regex = re.compile(r'^(PL )?[0-9]{2}-[0-9]{3}$')
    match = regex.search(code)
    if match is None:
        return False
    return True


class ValidatePostalCodeTest(unittest.TestCase):
    def testValidPostalCode(self):
        code = '''12-345'''
        result = validate_postal_code(code)
        self.assertTrue(result)

    def testInvalidPostalCode(self):
        code = '''12-3456'''
        result = validate_postal_code(code)
        self.assertFalse(result)
        code = '''ab-cde'''
        result = validate_postal_code(code)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
