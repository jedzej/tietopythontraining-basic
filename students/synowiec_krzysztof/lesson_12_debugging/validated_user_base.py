import re
import os
import argparse
import sys
import csv
import logging
from argparse import RawTextHelpFormatter

EMAIL = 'email'
PASS = 'password'
PHONE = 'phone'
POST = 'postal code'
FIELDNAMES = [EMAIL, PASS, PHONE, POST]


def main():
    file_name = 'data.csv'
    user_map = {}
    e, p, m, c, v = check_args(sys.argv[1:])
    log_configuration(v)
    combined_validator(e, p, m, c)
    if os.path.exists(file_name):
        with open(file_name, 'r') as csv_file:
            for row in csv.DictReader(csv_file):
                user_map[row[EMAIL]] = (row[PASS], row[PHONE], row[POST])
    logging.debug('Data file contains {} records'.format(len(user_map)))
    logging.info('{} {} {} {} accepted'.format(e, p, m, c))
    if e in user_map:
        logging.info('Email {} is in file. Data will be updated'.format(e))
    user_map[e] = (p, m, c)

    with open(file_name, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, FIELDNAMES)
        writer.writeheader()
        for email in user_map:
            passw, phone, postal = user_map.get(email)
            row = {EMAIL: email, PASS: passw, PHONE: phone, POST: postal}
            writer.writerow(row)


def check_args(args=None):
    parser = argparse.ArgumentParser(description='User base',
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('-e', '--email',
                        help='Email ex: example@gmail.com',
                        default='example@gmail.com')
    parser.add_argument('-p', '--passwd',
                        help='Password ex: Passwd123!',
                        default='Passwd123!')
    parser.add_argument('-m', '--mobile',
                        help='Phone number ex: +48 123 456 789',
                        default='+48 123 456 789')
    parser.add_argument('-c', '--code',
                        help='postal code',
                        default='59-101')
    parser.add_argument('-v', '--verbose', help='verbose output, log level:\n'
                        'info - all,\n'
                        'warning - errors,\n'
                        'disable - no', default='info')
    res = parser.parse_args(args)
    return res.email, res.passwd, res.mobile, res.code, res.verbose


def is_email_valid(email):
    regex = re.compile(r'[^@.\s][^@\s]+@[^@\s]+\.[^@\s]+')
    return regex.match(email)


def is_phone_valid(phone):
    regex = re.compile(r'(\+\d{2}\s)?\d{3}[\s-]?\d{3}[\s-]?\d{3}')
    return regex.match(phone)


def is_strong_password(passwd):
    has_at_least_eight = re.compile(r'.{8}')
    has_upper_case = re.compile(r'[A-Z]')
    has_lower_case = re.compile(r'[a-z]')
    has_digit = re.compile(r'\d')

    if not has_at_least_eight.search(passwd):
        logging.warning("Password is too short!")
        return False
    elif not has_upper_case.search(passwd):
        logging.warning("Password needs upper case letter!")
        return False
    elif not has_lower_case.search(passwd):
        logging.warning("Password needs lower case letter!")
        return False
    elif not has_digit.search(passwd):
        logging.warning("Password needs digit!")
        return False
    return True


def is_postal_code_valid(postal_code):
    regex = re.compile(r'\d{2}-\d{3}')
    return regex.match(postal_code)


def combined_validator(e, p, m, c):
    if not is_email_valid(e):
        raise Exception("Email is invalid")
    elif not is_strong_password(p):
        raise Exception("Password is too weak")
    elif not is_phone_valid(m):
        raise Exception("Phone is invalid")
    elif not is_postal_code_valid(c):
        raise Exception("Postal code is invalid")


def log_configuration(level):
    logging.basicConfig(format='%(asctime)s - %(levelname)s- %(message)s')
    log_level = get_log_level(level)
    logging.getLogger().setLevel(log_level)


def get_log_level(level):
    if level == 'disable':
        return logging.CRITICAL
    elif level == 'warning':
        return logging.WARNING
    elif level == 'info':
        return logging.INFO


if __name__ == '__main__':
    main()
