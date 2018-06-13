import re
import os
import argparse
import sys
import csv
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s- %(message)s')

EMAIL_K = 'email'
PASS_K = 'password'
PHONE_K = 'phone'
POST_K = 'postal code'
FILEDNAMES = [EMAIL_K, PASS_K, PHONE_K, POST_K]


def main():
    file_name = 'data.csv'
    user_map = {}

    if os.path.exists(file_name):
        for row in csv.DictReader(open(file_name, 'r')):
            user_map[row[EMAIL_K]] = (row[PASS_K], row[PHONE_K], row[POST_K])
    logging.debug('Data file contains {} records'.format(len(user_map)))

    e, p, m, c, v = check_args(sys.argv[1:])
    log_level = get_log_level(v)
    logging.getLogger().setLevel(log_level)
    combined_validator(e, p, m, c)
    logging.info('{} {} {} {} accepted'.format(e, p, m, c))
    if e in user_map:
        logging.info('Email {} is in file. Data will be updated'.format(e))
    user_map[e] = (p, m, c)

    writer = csv.DictWriter(open(file_name, 'w'), FILEDNAMES)
    writer.writeheader()
    for email in user_map:
        passw, phone, postal = user_map.get(email)
        row = {EMAIL_K: email, PASS_K: passw, PHONE_K: phone, POST_K: postal}
        writer.writerow(row)


def check_args(args=None):
    parser = argparse.ArgumentParser(description='User base')
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
    parser.add_argument('-v', '--verbose', help='verbose output, log level:'
                        'info - all,'
                        'warning - errors,'
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
        print("Password is too short!")
        return False
    elif not has_upper_case.search(passwd):
        print("Password needs upper case letter!")
        return False
    elif not has_lower_case.search(passwd):
        print("Password needs lower case letter!")
        return False
    elif not has_digit.search(passwd):
        print("Password needs digit!")
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


def get_log_level(level):
    if level == 'disable':
        return logging.CRITICAL
    elif level == 'warning':
        return logging.WARNING
    elif level == 'info':
        return logging.INFO


if __name__ == '__main__':
    main()
