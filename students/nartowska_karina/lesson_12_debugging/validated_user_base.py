import os
import argparse
import csv
import logging

from validators import email_validator
from validators import postal_code_validator
from validators import phone_number_validator
from validators import strong_password_detection

LOGGER_LEVELS = {"debug": logging.DEBUG,
                 "info": logging.INFO,
                 "warning": logging.WARNING,
                 "error": logging.ERROR}


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Validated user base')
    parser.add_argument('-v', '--verbose',
                        help='verbose output: debug, info, warning, error',
                        default='debug')

    result = parser.parse_args(args)
    return result.verbose


verbose = check_arg()
logging.basicConfig(level=LOGGER_LEVELS[verbose],
                    format='%(asctime)s - %(levelname)s - %(message)s')


def combined_validator(email, password, phone_number, postal_code):
    if not (email_validator(email)
            and strong_password_detection(password)
            and phone_number_validator(phone_number)
            and postal_code_validator(postal_code)):
        raise Exception("Incorrect data")


def write_to_csv(input):
    with open('data.csv', 'a+') as csv_file:
        fieldnames = ['email', 'password', 'phone_number', 'postal_code']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not os.stat(csv_file.name).st_size:
            writer.writeheader()
        writer.writerow(input)
    logging.debug("Writing complete")


def main():
    input_data = {"email": "karina@nartowska.com",
                  "password": "kfjdskfjdsDSFDSFsfsdf1212@@#4wdfsfds",
                  "phone_number": "012345678",
                  "postal_code": "00-000"}

    combined_validator(input_data["email"],
                       input_data["password"],
                       input_data["phone_number"],
                       input_data["postal_code"])

    write_to_csv(input_data)


if __name__ == '__main__':
    main()
