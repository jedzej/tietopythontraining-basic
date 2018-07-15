#!/usr/bin/env python3

import argparse
import csv
import logging
import sys
import os

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

    if not is_valid_email(email):
        raise Exception("Invalid email.")
        return
    if not is_strong_password(password):
        raise Exception("Invalid password.")
        return
    if not is_valid_phone_number(phone_number):
        raise Exception("Invalid phone number.")
        return
    if not is_valid_postal_code(postal_code):
        raise Exception("Invalid postal code.")
        return
    logging.info("Verification passed")


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

    user_data_list = []
    user_record_exist = False

    if not os.path.exists(csv_file):
        with open(csv_file, 'a') as file:
            pass

    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == email:
                row = email, password, phone_number, postal_code
                user_record_exist = True
                logging.warning('This email exist in database, will be altered')
            user_data_list.append(row)
        if not user_record_exist:
            user_data_list.append([email, password, phone_number, postal_code])

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user_data_list)


def main():
    log = parse_args(sys.argv[1:])
    logging.getLogger().setLevel(log)

    email = input("Input email (e.g. tieto@tieto.com): ")
    password = input("Input password (e.g. tuRbo_pass9#): ")
    phone_number = input("Input phone number (e.g. 123-123-123): ")
    postal_code = input("Input postal code (e.g. 58-100): ")

    try:
        combined_validator(email, password, phone_number, postal_code)
    except Exception as e:
        logging.warning("Verification failed.")
        logging.warning("Exception caught: " + str(e))
        return

    save_user_data(email, password, phone_number, postal_code)


if __name__ == "__main__":
    main()
