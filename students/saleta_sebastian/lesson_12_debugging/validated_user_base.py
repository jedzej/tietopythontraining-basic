import argparse
import csv
import logging
import os
import shutil
import sys

from lesson_08_regular_expressions import \
    strong_password_detection, email_validator, phone_number_validator,\
    postal_code_validator


sys.path.append('..')
logging.basicConfig(level=logging.DEBUG, format=(' %(asctime)s - %(levelname)s'
                                                 ' - %(message)s'))

TEST_FILES_DIRECTORY = 'test_files'
TEST_FILE_NAME = 'user_base.csv'
TEMP_FILE_NAME = 'temp_base.csv'
COLUMN_TITLE_ROW = "email, password, phone number, postal code \n"

logger = logging.getLogger('__name__')


def set_logger_level(lvl):
    if lvl == 0:
        logging.disable(logging.CRITICAL)
    elif lvl == 1:
        logger.setLevel('WARNING')
    elif lvl == 2:
        logger.setLevel('INFO')


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Script to validate and save'
                                                 ' user data in csv file')
    parser.add_argument('-v', '--verbose',
                        help=('Verbose level.'
                              '0 - disabled, '
                              '1 - warnings and errors enabled '
                              '2 - info enabled'),
                        type=int)
    results = parser.parse_args(args)
    return results.verbose


def validate_user_data(email, password, phone_number, postal_code):
    logging.info('Validating user data')
    if not email_validator.check_email(email):
        logging.info('Email adress is invalid')
        raise Exception('Email address is invalid')
    if not strong_password_detection.check_if_password_is_strong(password):
        logging.info('Password is too weak')
        raise Exception('Password is too weak')
    if not phone_number_validator.check_phone_number(phone_number):
        logging.info('Phone number is invalid')
        raise Exception('Phone number is invalid')
    if not postal_code_validator.check_postal_code(postal_code):
        logging.info('Postal code is invalid')
        raise Exception('Postal code is invalid')


def create_csv_file():
    if not os.path.isfile("user_base.csv"):
        open(os.path.join(TEST_FILE_NAME), 'w')
        logging.info('user_base.csv file created')


def save_user_data(email, password, phone_number, postal_code):
    logging.info('Creating dict with user_data')
    user_data = {
        'email': email,
        'password': password,
        'phone_number': phone_number,
        'postal_code': postal_code
    }
    logging.debug('User_data dict values: email: {}, password: {},'
                  ' phone_number{}, postal_code: {}'
                  .format(email, password, phone_number, postal_code))

    with open(TEST_FILE_NAME, 'r', newline='') as csvfile, \
            open(TEMP_FILE_NAME, 'w', newline='') as tempfile:
        logging.info('temp_base.csv created')
        reader = csv.DictReader(csvfile, fieldnames=user_data.keys())
        writer = csv.DictWriter(tempfile, fieldnames=user_data.keys())
        row = 0
        email_found = False

        for record in reader:
            row += 1
            logging.debug('Row {} in user_base.csv'.format(str(row)))
            if record['email'] == user_data['email']:
                logging.info('Email found in base')
                record = user_data
                email_found = True
                logging.debug('email_found flag: {}'.format(email_found))
            writer.writerow(record)
            logging.info('Record: {} saved in temp_base.csv'.format(record))
        if row == 0 or not email_found:
            logging.debug('Row {} in user_base.csv'.format(str(row)))
            logging.debug('email_found flag: {}'.format(email_found))
            writer.writerow(user_data)
            logging.info('Record: {} saved in temp_base.csv'.format(record))

    shutil.move(TEMP_FILE_NAME, TEST_FILE_NAME)
    logging.debug('Rename {} to {}'.format(TEMP_FILE_NAME, TEST_FILE_NAME))


def main():
    create_csv_file()
    verbose = check_arg(sys.argv[1:])
    set_logger_level(verbose)

    logger.info('Get email from user')
    user_email = input('Enter email: ')
    logger.info('Get password from user')
    user_password = input('Enter password: ')
    logger.info('Get phone number')
    user_phone_number = input('Enter phone number: ')
    logger.info('Get postal code')
    user_postal_code = input('Enter postal code: ')

    validate_user_data(
        user_email, user_password, user_phone_number, user_postal_code)
    save_user_data(
        user_email, user_password, user_phone_number, user_postal_code)


if __name__ == '__main__':
    main()
