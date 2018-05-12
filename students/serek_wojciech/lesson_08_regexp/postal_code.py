#!/usr/bin/env python3
"""Postal code validation exercise"""
import re


def validate_postal_code(code):
    """Validate postal code"""
    if re.compile(r'^\d{2}-?\d{3}$').match(code):
        return True
    return False


def main():
    """Main function"""
    codes = ['01-100', 'aa-222', '05-45a', '12445', '55-789', 'as88-789ss',
             '01-112s', 's44-789']
    for code in codes:
        print('Postal code: ' + code.ljust(15) + ' is valid: ' +
              str(validate_postal_code(code)))


if __name__ == '__main__':
    main()
