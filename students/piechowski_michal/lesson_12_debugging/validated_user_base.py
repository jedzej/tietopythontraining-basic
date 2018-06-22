#!/usr/bin/env python3

import argparse
import csv
import logging
import sys

from students.piechowski_michal.lesson_08_regular_expressions.email_validator\
    import is_valid as is_valid_email
from students.piechowski_michal.lesson_08_regular_expressions.phone_number_validator\
    import is_valid as is_valid_phone_number
from students.piechowski_michal.lesson_08_regular_expressions.postal_code_validator\
    import is_valid as is_valid_postal_code
from students.piechowski_michal.lesson_08_regular_expressions.strong_password_detection\
    import is_strong as is_strong_password

logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')


def combined_validator(email, password, phone_number, postal_code):
    logging.info("Verifying user data")

    if is_valid_email(email) and is_strong_password(password) \
            and is_valid_phone_number(phone_number) \
            and is_valid_postal_code(postal_code):
        logging.info("Verification passed")
    else:
        logging.warning("Verification failed")
        raise Exception("One of arguments didn't pass verification.")


def check_arg(args):
    parser = argparse.ArgumentParser(
        description='Script to save validated users to a CSV file')
    parser.add_argument('-l', '--log',
                        choices=['disabled', 'warning', 'info'],
                        help='Log verbosity',
                        default='info')

    results = parser.parse_args(args)

    if results.log == 'disabled':
        return logging.CRITICAL
    elif results.log == 'warning':
        return logging.WARNING
    else:
        return logging.INFO


def save_user_data(email, password, phone_number, postal_code):
    csv_file = 'userdata.csv'

    with open(csv_file, 'a') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([email, password, phone_number, postal_code])
        logging.warning("User data has been written")

    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        logging.info("Currently we have following rows:")
        for row in reader:
            logging.info(' '.join(row))


def main():
    verbosity = check_arg(sys.argv[1:])
    logging.getLogger().setLevel(verbosity)

    email = input("Input email (e.g. some@email.com): ")
    password = input("Input password (e.g. some_Pass8): ")
    phone_number = input("Input phone number (e.g. 123-456-789): ")
    postal_code = input("Input postal code (e.g. 12-200): ")

    try:
        combined_validator(email, password, phone_number, postal_code)
    except Exception:
        logging.warning("Exception arised, not saving the user data")
        return

    save_user_data(email, password, phone_number, postal_code)


if __name__ == "__main__":
    main()
