#!/usr/bin/env python3


import sys
import shutil
import argparse
import logging
import csv
sys.path.append('..')
from lesson_08_regular_expressions import email_validator,\
    strong_password_detection, phone_number_validator,\
    postal_code_validator_poland


logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


DEFAULT_DEBUG_LVL = 1
CSV_FILE = "database.csv"
TMP_FILE = "tmp.csv"


class ValidationError(Exception):
    def __init__(self, message):
        super(ValidationError, self).__init__(
            "'{}' is incorrect, please change it and retry."
            .format(message))


def check_arg(args=None):
    parser = argparse.ArgumentParser(description="Script for adding entries"
                                     " to CSV database")
    parser.add_argument('-e', '--email',
                        help="email address",
                        required=True)
    parser.add_argument('-p', '--password',
                        help="user's password",
                        required=True)
    parser.add_argument('-n', '--phone_number',
                        help="user's phone number",
                        required=True)
    parser.add_argument('-c', '--postal_code',
                        help="user's postal code",
                        required=True)
    parser.add_argument('-v', '--verbosity',
                        help="debug level:\n0 - disabled,\n"
                        "1 - errors/warnings [default],\n"
                        "2 - all debugs",
                        type=int,
                        default=DEFAULT_DEBUG_LVL,
                        required=False)

    return(vars(parser.parse_args(args)))


def set_debug_level(dbg_lvl):
    if dbg_lvl not in [0, 1, 2]:
        logger.error("Incorrect verbosity lvl, using default one")
        dbg_lvl = DEFAULT_DEBUG_LVL

    if dbg_lvl == 2:
        logger.setLevel(logging.DEBUG)
    elif dbg_lvl == 1:
        logger.setLevel(logging.WARNING)
    elif dbg_lvl == 0:
        logging.disable(logging.CRITICAL)


def combined_validator(dict_entry):
    for x, y in dict_entry.items():
        globals()[x] = y

    if not email_validator.email_validator(email):
        raise ValidationError(email)
    if not strong_password_detection.strong_password_detection(password):
        raise ValidationError(password)
    if not phone_number_validator.phone_number_validator(phone_number):
        raise ValidationError(phone_number)
    if not postal_code_validator_poland.postal_code_validator_poland(
            postal_code):
        raise ValidationError(postal_code)


def update_database(dict_entry):
    open(CSV_FILE, 'a').close()  # create file if it doesn't exist

    with open(CSV_FILE, 'r') as csv_file, open(TMP_FILE, 'w')\
            as tmp_file:
        reader = csv.DictReader(csv_file, fieldnames=sorted(dict_entry.keys()))
        writer = csv.DictWriter(tmp_file, fieldnames=sorted(dict_entry.keys()))

        writer.writeheader()

        if not next(reader, None):
            logger.info("Csv file was empty, writing it's first entry!")
            writer.writerow(dict_entry)
        else:
            record_existed = False
            for row in reader:
                if row['email'] == dict_entry['email']:
                    logger.info("Updating already existing record")
                    writer.writerow(dict_entry)
                    record_existed = True
                else:
                    logger.info("Rewrite row")
                    writer.writerow(row)
            if not record_existed:
                logger.info("Appending new entry into database")
                writer.writerow(dict_entry)

    shutil.move(TMP_FILE, CSV_FILE)


def main():
    input_dict = check_arg(sys.argv[1:])

    set_debug_level(input_dict['verbosity'])
    input_dict.pop('verbosity')
    combined_validator(input_dict)
    update_database(input_dict)


if __name__ == "__main__":
    main()
