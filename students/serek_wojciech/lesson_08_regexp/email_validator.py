#!/usr/bin/env python3
"""Email validation exercise"""
import re


def validate_email(email):
    """Validate email address"""
    if re.compile(r'^[A-Za-z0-9_!#$%&\'*+/=?`{|}~^.-]+@[A-Za-z0-9.-]+$').\
            match(email):
        return True
    return False


def main():
    """Main function"""
    emails = ['test@test.org', 'test.test.org', 'test.test@test.org',
              'test_1@test.com', '_Email_test.1@test.com']
    for email in emails:
        print('Password: ' + email.ljust(25) + ' is valid: ' +
              str(validate_email(email)))


if __name__ == '__main__':
    main()
