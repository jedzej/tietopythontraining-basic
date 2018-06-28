#!/usr/bin/env python3

"""
regex_validators.py: practice projects: "Email validator", "Postal code
validator" and "Phone number validator" from:
Lesson 8 - Regular expressions
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


def check_validator(validator, valid_items, invalid_items, item_name):
    """
    This function checks if the received validation function works as expected
    and prints the result.
    :param validator: a function taking one string parameter and returning bool
    :param valid_items: list of strings for which the tested function is
    expected to return True
    :param invalid_items: list of strings for which the tested function is
    expected to return False
    :param string item_name: name of items type, eg. postcode, password etc
    :return: None
    """
    validation_ok = True

    for item in valid_items:
        if not validator(item):
            validation_ok = False
            print("The {} '{}' incorrectly classified as invalid".format(
                item_name, item))

    for item in invalid_items:
        if validator(item):
            validation_ok = False
            print("The {} '{}' incorrectly classified as valid"
                  .format(item_name, item))

    if validation_ok:
        print("Each {} classified correctly".format(item_name))


def main():

    # Email validator
    # examples of valid/invalid email addresses from:
    # https://en.wikipedia.org/wiki/Email_address
    valid_email_addr = ['simple@example.com', 'very.common@example.com',
                        'disposable.style.email.with+symbol@example.com',
                        'other.email-with-dash@example.com',
                        'fully-qualified-domain@example.com',
                        'user.name+tag+sorting@example.com', 'x@example.com',
                        r'"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@'
                        'strange.example.com',
                        'example-indeed@strange-example.com',
                        'admin@mailserver1',
                        "#!$%&'*+-/=?^_`{}|~@example.org",
                        r'"()<>[]:,;@\\\"!#$%&\'-/=?^_`{}| ~.a"@example.org',
                        'example@s.solutions',
                        'user@localserver']

    invalid_email_addr = ['Abc.example.com', 'A@b@c@example.com',
                          r'a"b(c)d,e:f;g<h>i[j\k]l@example.com',
                          'just"not"right@example.com',
                          r'this is"not\allowed@example.com',
                          r'this\ still\"not\\allowed@example.com',
                          '12345678901234567890123456789012345678901234567890'
                          '12345678901234+x@example.com',
                          'john..doe@example.com',
                          'john.doe@example..com',
                          '" "@example.org']

    check_validator(is_valid_email_addr, valid_email_addr, invalid_email_addr,
                    "email address")

    # Postal code validator
    valid_postcodes = ['71-123', '00-001', '12-345']
    invalid_postcodes = ['71123', '71-12', '7-1234', '7-12', '7-123', '-123',
                         '-', ' ', '', '71-', '712-123', 'ab-cde', '7A-123']

    check_validator(is_valid_postal_code, valid_postcodes, invalid_postcodes,
                    'postal code')

    # Phone number validator
    valid_phone_nums = ['123-456-789', '+48 123 456 789', '(+48)123-456-789',
                        '123456789', '+48123456789', '(+48)123456789',
                        '+48 123-456-789', '(+48) 123 456 789',
                        '0048 123 456 789']
    invalid_phone_nums = ['abc def ghi', ' ', '', '12-34-56-78', '+48-123-456',
                          '0048 123 456', '48-123-456-789', '(+48) 123 456',
                          '+48 xxx xxx xxx']

    check_validator(is_valid_phone_number, valid_phone_nums,
                    invalid_phone_nums, "phone number")


if __name__ == '__main__':
    main()
