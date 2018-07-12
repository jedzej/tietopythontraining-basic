#!/usr/bin/env python3

import argparse
import csv
import logging
import sys

from lesson_08.email_validator\
    import email_validate as is_valid_email
from lesson_08.phone_number_validator\
    import validate_phone_number as is_valid_phone_number
from lesson_08.postal_code_validator\
    import validate_postal_code_pl as is_valid_postal_code
from lesson_08.strong_password_detection\
    import password_checker as is_strong_password

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


def parse_args(args):
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
        pass

    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        rows = [x for x in list(reader) if not x[0] == email]

    with open(csv_file, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        if rows:
            writer.writerows(rows)

    with open(csv_file, 'a') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([email, password, phone_number, postal_code])
        logging.warning("User data written.")

    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        logging.info("Current rows:")
        for row in reader:
            logging.info(' '.join(row))


def main():
    log = parse_args(sys.argv[1:])
    logging.getLogger().setLevel(log)

    email = input("Input email (e.g. tieto@tieto.com): ")
    password = input("Input password (e.g. tuRbo_pass9#): ")
    phone_number = input("Input phone number (e.g. 123-123-123): ")
    postal_code = input("Input postal code (e.g. 58-100): ")

    try:
        combined_validator(email, password, phone_number, postal_code)
    except Exception:
        logging.warning("Exception caught, not")
        return

    save_user_data(email, password, phone_number, postal_code)


if __name__ == "__main__":
    main()
