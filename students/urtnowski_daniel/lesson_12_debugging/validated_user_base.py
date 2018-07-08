#!/usr/bin/env python3

"""
validated_user_base.py: a practice project: "Validated user base" from:
Lesson 12 - Debugging

This program takes email, password, phone number and postal code, validates
these fields and if validation passes, saves it to a file as CSV with email
considered as unique field.

Usage:
validated_user_base.py [-h] -e EMAIL -p PASSWORD -n PHONE_NUM -c POSTAL_CODE
[-V {0,1,2}]

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import argparse
import csv
import os
import shutil
import sys
import validators
from verbose_output import Logger


DATA_FILE = 'data.csv'
TMP_FILE = 'tmp.dat'


def get_args():
    parser = argparse.ArgumentParser(
        description='This program takes email, password, phone number and '
                    'postal code, validates these fields and if validation '
                    'passes, saves it to a file as CSV with email considered '
                    'as unique field.')

    parser.add_argument('-e', '--email', help='email address', required='True')
    parser.add_argument('-p', '--password', help='password', required='True')
    parser.add_argument('-n', '--phone_num', help='phone number',
                        required='True')
    parser.add_argument('-c', '--postal_code', help='postal code',
                        required='True')
    parser.add_argument('-V', '--verbose-output', dest='log_level',
                        help='logging level: 0 - disable, 1 - info, 2 - '
                             'warning. By default the logging is disabled',
                        type=int, choices=(0, 1, 2), default=0)

    args = parser.parse_args(sys.argv[1:])
    data = {
        'email': args.email,
        'password': args.password,
        'phone_num': args.phone_num,
        'postal_code': args.postal_code,
    }
    log_level = Logger.LogLevel(args.log_level)

    return data, log_level


def save_data(data, logger):

    logger.info("Record to be saved in the file: {}"
                .format(','.join(data.values())))

    if not os.path.exists(DATA_FILE):
        logger.info('The data file does not exist. Creating new file')
        data_file = open(DATA_FILE, 'w', newline='')
        writer = csv.DictWriter(data_file, fieldnames=data.keys())
        reader = None

    else:
        data_file = open(DATA_FILE, 'r', newline='')
        logger.info('File "{}" opened for reading'.format(DATA_FILE))

        tmp_file = open(TMP_FILE, 'w', newline='')
        logger.info('File "{}" opened for writing'.format(TMP_FILE))

        reader = csv.DictReader(data_file, fieldnames=data.keys())
        writer = csv.DictWriter(tmp_file, fieldnames=data.keys())

    writer.writeheader()

    found = False

    if reader is not None:
        next(reader)  # omit the header
        logger.info('Emails present in file:')
        for row in reader:
            logger.info(row['email'])
            if not found and row['email'] == data['email']:
                logger.info('The email is present in the file, updating '
                            'record')
                for k, v in data.items():
                    row[k] = v
                found = True

            writer.writerow(row)

    if not found:
        if reader is not None:
            logger.info('The email is not present in file, writing new record')
        writer.writerow(data)

    logger.info('Closing file: {}'.format(data_file.name))
    data_file.close()

    if reader is not None:
        logger.info('Closing file: {}'.format(tmp_file.name))
        tmp_file.close()

        logger.info('Replacing data file with temporary file')
        shutil.move(TMP_FILE, DATA_FILE)


def combined_validator(email, password, phone_num, postal_code):

    for item, name, validator in [
        (email, 'email', validators.is_valid_email_addr),
        (password, 'password', validators.is_password_strong),
        (phone_num, 'phone number', validators.is_valid_phone_number),
        (postal_code, 'postal code', validators.is_valid_postal_code)
    ]:
        if not validator(item):
            raise Exception('The {}: "{}" is incorrect'.format(name, item))


def main():

    data, log_level = get_args()
    logger = Logger(log_level)
    logger.info('Program start')

    data_str = ', '.join(['{}: "{}"'.format(k, v) for k, v in data.items()])
    logger.info('Params: {}'.format(data_str))

    try:
        logger.info('Validating received parameters')
        combined_validator(email=data['email'], password=data['password'],
                           phone_num=data['phone_num'],
                           postal_code=data['postal_code'])
        logger.info('Validation successful')

        logger.info('Saving data to CSV file')
        save_data(data, logger)

    except Exception as ex:
        logger.warning('Critical error: {}'.format(ex))

    logger.info('Program end')


if __name__ == '__main__':
    main()
