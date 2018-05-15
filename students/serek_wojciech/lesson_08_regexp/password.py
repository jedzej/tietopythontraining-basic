#!/usr/bin/env python3
"""Strip method exercise"""
import re


def check_password(password):
    """Check if password is strong"""

    strength = (len(password) >= 8 and
                re.compile(r'.*[a-z]').match(password) and
                re.compile(r'.*[A-Z]').match(password) and
                re.compile(r'.*\d+').match(password) and
                re.compile(r'.*[_!@#$%^&*]').match(password))

    if strength:
        return True
    return False


def main():
    """Main function"""
    passwords = ['pass', 'Pass', 'Pass2',
                 'password', 'Password', 'Password2',
                 'longpassword', 'Long!Password', 'Long^Password5',
                 'LongPassword_10', 'TestP@sswo3rd', '!@#$%^&*_']

    for password in passwords:
        print('Password: ' + password.ljust(20) + ' is strong: ' +
              str(check_password(password)))


if __name__ == '__main__':
    main()
