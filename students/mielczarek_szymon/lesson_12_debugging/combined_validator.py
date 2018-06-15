#! python3
import sys
import shutil
import logging
import argparse
import csv
sys.path.append('..')
from lesson_08_regular_expressions import \
    email_validator, strong_password_detection, phone_number_validator,\
    postal_code_validator

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)


USERDATA_CSV_FILE = 'userdata.csv'
TMPFILE = 'tmp.csv'


class ValidatorError(Exception):
    """Custom exception raised in case of validator check failure."""

    def __init__(self, err_msg):
        super(ValidatorError, self).__init__("Validator Error: {}". format(err_msg))


def combined_validator(email, password, phone_number, postal_code):
    logger.info("Validating user data...")
    if not email_validator.validate_email_address(email):
        raise ValidatorError("Supplied e-mail address is invalid.")
    if not strong_password_detection.check_password_strength(password):
        raise ValidatorError("Supplied password is too weak.")
    if not phone_number_validator.validate_phone_number(phone_number):
        raise ValidatorError("Supplied phone number is invalid.")
    if not postal_code_validator.validate_postal_code_pl(postal_code):
        raise ValidatorError("Supplied postal code is invalid.")
    logger.info("User data validated OK.")


def set_verbosity_level(verbose_lvl):
    if verbose_lvl == 0:
        logging.disable(logging.CRITICAL)
    elif verbose_lvl == 1:
        logger.setLevel(logging.WARNING)
    elif verbose_lvl == 2:
        logger.setLevel(logging.INFO)


def save_user_data(data):
    """Add new user data record or update existing one based on the email field"""

    with open(USERDATA_CSV_FILE, 'r', newline='') as csvfile,\
            open(TMPFILE, 'w', newline='') as tmpfile:
        reader = csv.DictReader(csvfile, fieldnames=data.keys())
        writer = csv.DictWriter(tmpfile, fieldnames=data.keys())
        rows_num = 0
        user_found = False
        for record in reader:
            if record['email'] == data['email']:
                logger.info("Email {} exists in the user base, replacing data.".
                            format(record['email']))
                record = data
                user_found = True
            writer.writerow(record)
            rows_num += 1

        if rows_num == 0 or not user_found:
            logger.info("Adding user to the data base.")
            writer.writerow(data)

    shutil.move(TMPFILE, USERDATA_CSV_FILE)


def main():
    parser = argparse.ArgumentParser(description='Combined Validator program.')
    parser.add_argument('-v', '--verbosity',
                        help="Verbosity level. 0 - disabled, 1 - warnings and errors, "
                             "2 - info. Warnings and errors are enabled by default.",
                        type=int, choices=(0, 1, 2), default=1)
    args = parser.parse_args()

    set_verbosity_level(args.verbosity)

    logger.info("Program started")
    while True:
        email = input("Enter email: ")
        password = input("Enter password: ")
        phone_number = input("Enter phone number: ")
        postal_code = input("Enter postal code: ")

        is_data_valid = True
        try:
            combined_validator(email, password, phone_number, postal_code)
        except ValidatorError as err:
            logger.error('\n' + str(err))
            key = input("\nDo you want to try again? Type yes or no: ")
            if key == "yes":
                continue
            is_data_valid = False
        break

    if is_data_valid:
        user_data = {
            'email': email,
            'password': password,
            'phone_number': phone_number,
            'postal_code': postal_code
        }
        save_user_data(user_data)

    logger.info("Program done")


if __name__ == "__main__":
    main()
