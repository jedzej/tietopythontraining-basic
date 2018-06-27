import logging
import re
import argparse
import sys


def logger_lever_chooser(level):
    if level == 'd':
        logging.basicConfig(level=logging.CRITICAL,
                            format=' %(asctime)s - %(levelname)s- %(message)s')
    elif level == 'w':
        logging.basicConfig(level=logging.WARNING,
                            format=' %(asctime)s - %(levelname)s- %(message)s')
    elif level == 'i':
        logging.basicConfig(level=logging.INFO,
                            format=' %(asctime)s - %(levelname)s- %(message)s')


def check_arg(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--email', dest='email',
                        help='Email',
                        default='example@gmail.com')
    parser.add_argument('-p', '--password', dest='password',
                        help='Password',
                        default='AaBb!123')
    parser.add_argument('-n', '--number', dest='phone_number',
                        help='Phone number',
                        default='600111222')
    parser.add_argument('-v', '--verbose', dest='verbose',
                        help='Logging level', choices=['d', 'w', 'i'],
                        default='i')
    r = parser.parse_args(args)
    return r.email, r.password, r.phone_number, r.verbose


def email_validator(text):
    email_regex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+'
                             r'(\.[a-zA-Z]{2,4}))')
    try:
        if text == email_regex.search(text).group(0):
            return 'Valid email'
    except AttributeError:
        raise Exception('Invalid email')


def check_single_regex(text, pattern):
    regex = re.compile(pattern)
    return re.findall(regex, text)


def strong_password_detection(text):
    amount_list = [len(check_single_regex(text, i)) for i in
                   ['[a-z]', '[A-Z]', '\d']]
    if len(text) < 8:
        raise Exception('Too short')
    elif not all(amount_list):
        raise Exception("Password should contain at least one digit, "
                        "uppercase and lowercase characters")
    else:
        return "Password is strong"


def phone_number_validator(text):
    phone_regex = re.compile(r'\(?(\d{4}|\+\d{2})?\)?\s?'
                             r'(\d{9}|(\d{3}(\s|-)\d{3}(\s|-)\d{3}))')
    try:
        if text == phone_regex.search(text).group(0):
            return 'Valid phone number'
    except AttributeError:
        raise Exception('Invalid phone number')
    else:
        raise Exception('Invalid phone number')


def write_or_replace_record(accounts, given_values):
    result = ''
    email_exist = False
    for account in accounts:
        if account == '':
            continue
        if given_values[0] in account:
            result += ', '.join(given_values) + '\n'
            email_exist = True
        else:
            result += account + '\n'
    return result, email_exist


def update_csv(given_values):
    try:
        with open('data.csv', 'r') as file:
            records = file.read().split('\n')
    except Exception:
        with open('data.csv', 'w+') as file:
            records = file.read().split('\n')
    result, email_in_old_data = write_or_replace_record(records, given_values)
    if not email_in_old_data:
        result += ', '.join(given_values)
    with open('data.csv', 'w') as file:
        file.write(result)
    logging.info("CSV updated")


def combined_validator():
    email, password, phone_number, log = check_arg(sys.argv[1:])
    logger_lever_chooser(log)
    logging.info('Start of program')
    try:
        logging.info('Email validation...')
        email_validator(email)
        logging.info('Correct email')
        logging.info('Passport validation...')
        strong_password_detection(password)
        logging.info('Correct passport')
        logging.info('Phone number validation...')
        phone_number_validator(phone_number)
        logging.info('Correct phone number')
        update_csv([email, password, phone_number])
    except Exception:
        logging.warning('Invalid values')


combined_validator()
