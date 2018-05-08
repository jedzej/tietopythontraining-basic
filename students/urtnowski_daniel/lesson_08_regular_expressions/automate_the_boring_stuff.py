#!/usr/bin/env python3

"""
automate_the_boring_stuff.py: a practice projects: "Regex version of strip"
and "Strong Password Detection" from:
https://automatetheboringstuff.com/chapter7/
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import re


def regex_strip(input_str, chars=' '):
    """
    This function takes a string and does the same thing as the strip() string
    method.
    :param string input_str: a string to be stripped
    :param string chars: characters to be removed form the beginning and the
    end of the input string
    :return string: the modified string
    """
    escaped_chars = re.escape(chars)

    strip_regex = re.compile('^([{0}]+)'.format(escaped_chars))
    modified_str = strip_regex.sub('', input_str)

    strip_regex = re.compile('([{0}]+)$'.format(escaped_chars))
    modified_str = strip_regex.sub('', modified_str)

    return modified_str


def is_password_strong(password):
    """
    This function checks if input string is a strong password
    :param password: a string with password for verification
    :return bool: True if the passed string is a strong password, False
    otherwise
    """
    is_strong = True

    patterns = [r'^.{8,}$', r'\d+', r'[a-z]+', r'[A-Z]+']
    for pattern in patterns:
        passwd_regex = re.compile(pattern)
        mo = passwd_regex.search(password)

        if mo is None:
            is_strong = False
            break

    return is_strong


def main():

    # Regex version of strip
    for string, chars in [('0900-123-456-789-090-00', '0-9'),
                          ('   ala ma  kota    ', ' '), ('***aa*.a...', '*.a'),
                          ('bcd ala ma kota cbdc dcdc db ', 'bcd '),
                          ('***** ala ma kota ********', ' *')]:
        print("'{}' with stripped char(s): '{}' is: '{}'"
              .format(string, chars, regex_strip(string, chars)))

    for string in ['ala ma kota    ', '   ala ma kota', '   ala ma kota    ']:
        print("'{}' with stripped white spaces is: '{}'"
              .format(string, regex_strip(string)))

    print('')

    # Strong Password Detection
    for password in ['Password5', 'weaK123', '123456789', 'AbcDefghijk',
                     'Admin1', 'A1B2C3D4E5', '1a2b3c4d5e', 'stR0ngPass', '  ']:
        print("'{}' is strong password: {}"
              .format(password, is_password_strong(password)))


if __name__ == '__main__':
    main()
