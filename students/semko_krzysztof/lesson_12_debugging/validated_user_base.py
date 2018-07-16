"""
Validated user base - write script that takes email,
password, phone number and postal code, validates these
fields and if validation passes, saves it to a file as CSV
with email considered as unique field. If a record with the
same email is already in the file, the old record should be
altered by new one. Use validators implemented in lesson 8,
exercises 2, 3, 4 and 5. As part of this exercise write
combined_validator function that takes email, password,
phone number and postal code and throws exceptions if
any of arguments doesn't pass validation. Add 'verbose output'.
"""

import argparse
import csv
import logging
import os
import sys

from validate_data import check_email
from validate_data import check_number
from validate_data import check_postal_code
from validate_data import check_password

LOG_LEVELS = {"debug": logging.DEBUG,
              "info": logging.INFO,
              "warning": logging.WARNING,
              "error": logging.ERROR,
              "critical": logging.CRITICAL}

FILE_PATH = "personal_data.csv"


def args_parameters(args):
    parser = argparse.ArgumentParser(
        description='Validate data ')
    parser.add_argument('-l', '--logger',
                        help="Log level: debug, info, warning, "
                             "error, critical",
                        default="warning",)
    result = parser.parse_args()

    return result.logger


log_level = args_parameters(sys.argv)
logging.basicConfig(level=LOG_LEVELS[log_level], format='%(asctime)s '
                    '- %(levelname)s - %(message)s')


def write_csv(data):
    if not os.path.isfile(FILE_PATH):
        file = open(FILE_PATH, "a")
        with file:
            writer = csv.DictWriter(file, fieldnames=data)
            writer.writeheader()

    unique_id = data["email"]
    if duplicate_check(unique_id, FILE_PATH):
        return

    file = open(FILE_PATH, "a")
    with file:
        writer = csv.DictWriter(file, fieldnames=data)
        writer.writerow(data)


def duplicate_check(uid, path):
    with open(path) as File:
        reader = csv.DictReader(File)
        for row in reader:
            if (row["email"]) == uid:
                return True
    return False


def combined_validator(email, phone_number, postal_code, password):
    if (check_email(email) and check_number(phone_number) and
            check_postal_code(postal_code) and check_password(password)):
        logging.debug("Input data is correct")
    else:
        raise Exception("Personal data is not correct")


def input_data_manual():
    print("Please input personal data:")
    email = str(input())
    phone_number = str(input())
    postal_code = str(input())
    password = str(input())
    data = {"email": email, "phone number": phone_number,
            "postal code": postal_code, "password": password}
    return data


def main():
    # input_data = input_data_manual()
    # For testing purposes, let's use fixed dictionary
    input_data = {"email": "example@mail.com", "phone number": "123456789",
                  "postal code": "12-345", "password": "Hello1234"}
    combined_validator(input_data["email"],
                       input_data["phone number"],
                       input_data["postal code"],
                       input_data["password"])

    write_csv(input_data)


if __name__ == '__main__':
    main()
