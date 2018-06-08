#!/usr/bin/env python3

import re
import unittest


def check_password(password):
    # check length
    regex = re.compile(r'[a-zA-Z0-9]{8,}')
    match = regex.search(password)
    if match is None:
        return False
    # check for any small letter
    regex = re.compile(r'.*?([a-z]).*?')
    match = regex.search(password)
    if match is None:
        return False
    # check for any big letter
    regex = re.compile(r'.*?([A-Z]).*?')
    match = regex.search(password)
    if match is None:
        return False
    # check for anynumber
    regex = re.compile(r'.*?([0-9]).*?')
    match = regex.search(password)
    if match is None:
        return False
    return True


class CheckPasswordTest(unittest.TestCase):
    def testGoodPasswords(self):
        result = check_password("1Bcdefgh")
        self.assertTrue(result)
        result = check_password("abcdefG1")
        self.assertTrue(result)
        result = check_password("AbCdEfG1")
        self.assertTrue(result)
        result = check_password("1BcDeFgH")
        self.assertTrue(result)
        result = check_password("123aA678")
        self.assertTrue(result)
        result = check_password("123dE678")
        self.assertTrue(result)
        result = check_password("123De678")
        self.assertTrue(result)

    def testBadPasswords(self):
        result = check_password("1Bcdef")
        self.assertFalse(result)
        result = check_password("abcdef")
        self.assertFalse(result)
        result = check_password("AbCdEf")
        self.assertFalse(result)
        result = check_password("1BcDeF")
        self.assertFalse(result)
        result = check_password("123aA6")
        self.assertFalse(result)
        result = check_password("123dE6")
        self.assertFalse(result)
        result = check_password("123De6")
        self.assertFalse(result)
        result = check_password("1234567890")
        self.assertFalse(result)
        result = check_password("abcdefghij")
        self.assertFalse(result)
        result = check_password("ABCDEFGHIJ")
        self.assertFalse(result)
        result = check_password("abcdeFGHIJ")
        self.assertFalse(result)
        result = check_password("ABCDEfghij")
        self.assertFalse(result)
        result = check_password("12345FGHIJ")
        self.assertFalse(result)
        result = check_password("12345fghij")
        self.assertFalse(result)
        result = check_password("abcde67890")
        self.assertFalse(result)
        result = check_password("ABCDE67890")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
