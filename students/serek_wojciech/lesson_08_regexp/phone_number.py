#!/usr/bin/env python3
"""Phone number validation exercise"""
import re


def validate_phone_number(code):
    """Validate phone number"""
    if re.compile(r'^(\+\d{2}[- ]?)?(\d{3}[- ]?){2}\d{3}$').match(code):
        return True
    return False


def main():
    """Main function"""
    phones = ['+48123456789', '123456789', '48123456789',
              '+48 123 456 789', '+48 123456789', '+48 123 456 78a',
              '+48-123 456 789', '+48 123-456-789', '+48-123-456-789',
              '+4 123 456 789']
    for phone in phones:
        print('Password: ' + phone.ljust(20) + ' is valid: ' +
              str(validate_phone_number(phone)))


if __name__ == '__main__':
    main()
