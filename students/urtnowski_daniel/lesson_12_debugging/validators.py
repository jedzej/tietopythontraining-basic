#!/usr/bin/env python3

"""
validators.py: helper functions for validating email address, password,
postal code and phone number

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import re


def is_valid_email_addr(email_addr):
    """
    This function checks if supplied string is valid e-mail address
    :param string email_addr: email address for verification
    :return bool: True if the passed string is a valid email address, False
    otherwise
    """
    is_addr_valid = False

    addr_regex = re.compile(r'^(.{1,64})@(.{1,255})$')
    mo = addr_regex.search(email_addr)

    if mo is not None:
        local_part, domain = mo.groups()

        char_set = r'[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]'
        local_part_regex = re.compile('^((({0}+)([.]?)({0}?))+|(".*\S+.*"))$'
                                      .format(char_set))
        mo = local_part_regex.search(local_part)

        if mo is not None:
            domain_regex = re.compile(r'^(([a-zA-Z0-9-]{1,63}[.]?)*'
                                      '[a-zA-Z0-9-]{1,63})$')
            mo = domain_regex.search(domain)

            if mo is not None:
                is_addr_valid = True

    return is_addr_valid


def is_valid_postal_code(postal_code):
    """
    This function checks if supplied string is valid postal code
    :param string postal_code: postal code for verification
    :return bool: True if the passed string is a valid postal code, False
    otherwise
    """
    is_code_valid = False
    postcode_regex = re.compile(r'^\d{2}-\d{3}$')

    if postcode_regex.search(postal_code) is not None:
        is_code_valid = True

    return is_code_valid


def is_valid_phone_number(phone_number):
    """
    This function checks if supplied string is valid phone number
    :param string phone_number: phone number for verification
    :return bool: True if the passed string is a valid phone number, False
    otherwise
    """
    is_number_valid = False
    phone_number_regex = re.compile(r'^(\(?(00|\+)\d{2}\)?[ ]?)?'
                                    '\d{3}(-| )?\d{3}(-| )?\d{3}$')
    if phone_number_regex.search(phone_number) is not None:
        is_number_valid = True

    return is_number_valid


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


if __name__ == '__main__':
    pass
