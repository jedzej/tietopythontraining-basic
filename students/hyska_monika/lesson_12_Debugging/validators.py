import re
import logging


def password_check(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    password_ok = not (length_error or digit_error or
                       uppercase_error or lowercase_error)
    password_status = {'Password is strong.': password_ok,
                       'length to short': length_error,
                       'missing digits': digit_error,
                       'missing uppercase': uppercase_error,
                       'missing lowercase': lowercase_error}
    result = [k for k, v in password_status.items() if v is True]
    print(', '.join(result))
    logging.info('Password info: %s' % result)
    if password_ok is True:
        logging.info('Password is valid')
        return True
    else:
        logging.info('Pasword isnt valid')
        return False


def check_email(email):
    email_regex = re.compile(r'''
        [a-zA-Z0-9._%+-]+      # username
        @                       # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        \.[a-zA-Z]{2,4}$       # dot and 2 - 4 letters
        ''', re.VERBOSE)
    email_result = email_regex.match(email)
    if email_result is not None:
        print("Email is valid.")
        logging.info('Email: %s is valid' %email)
        return True
    else:
        print("Email isn't valid.")
        logging.info('Email: %s isnt valid' % email)
        return False


def check_postal_code(postal_code):
    post_code_regex = re.compile(r'(\d{2})-(\d{3}$)')
    post_code_result = post_code_regex.match(postal_code)
    if post_code_result is not None:
        print("Postal code is valid.")
        logging.info('Postal code: %s is valid' % postal_code)
        return True
    else:
        print("Postal code isn't valid.")
        logging.info('Postal code: %s isnt valid' % postal_code)
        return False


def check_phone_number(phone_number):
    phone_number_regex = re.compile(r'''(
        (((00|\+)\d{2}\s)|(\((00|\+)\d{2}\)(\s)?))? # country code
        \d{3}               # first 3 digits
        ((-|\s)?\d{3}){2}$  # 2 groups: space or - and 3 digits
        )''', re.VERBOSE)
    phone_number_result = phone_number_regex.match(phone_number)
    if phone_number_result is not None:
        print("Phone number is valid.")
        logging.info('Phone number: %s is valid' % phone_number)
        return True
    else:
        print("Phone number isn't valid.")
        logging.info('Phone number: %s isnt valid' % phone_number)
        return False
