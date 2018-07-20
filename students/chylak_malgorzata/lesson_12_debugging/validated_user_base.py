import argparse
import csv
import logging
import os
import sys

from validate_data import validate_email
from validate_data import validate_number
from validate_data import validate_postal_code
from validate_data import validate_password

LOG_LEVELS = {"debug": logging.DEBUG,
              "info": logging.INFO,
              "warning": logging.WARNING,
              "error": logging.ERROR,
              "critical": logging.CRITICAL}

FILE_PATH = "user_base.csv"


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
    if (validate_email(email) and validate_number(phone_number) and
            validate_postal_code(postal_code) and validate_password(password)):
        logging.debug("Correct")
    else:
        raise Exception("Incorrect data")


def input_data():
    print("Please insert data:")
    email = str(input())
    phone_number = str(input())
    postal_code = str(input())
    password = str(input())
    data = {"email": email, "phone number": phone_number,
            "postal code": postal_code, "password": password}
    return data


def main():
    input_data = {"email": "sample@mail.com", "phone number": "111111111",
                  "postal code": "00-000", "password": "Adminadmin1"}
    combined_validator(input_data["email"],
                       input_data["phone number"],
                       input_data["postal code"],
                       input_data["password"])

    write_csv(input_data)


if __name__ == '__main__':
    main()
