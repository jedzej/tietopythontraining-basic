#!/usr/bin/env python3
"""Verify user base exercise"""
import argparse
import logging
import os
import csv
from lesson_08_regexp.email_validator import validate_email
from lesson_08_regexp.phone_number import validate_phone_number
from lesson_08_regexp.password import check_password
from lesson_08_regexp.postal_code import validate_postal_code

logging.basicConfig(format=' %(asctime)s - %(levelname)s - %(message)s')


def combined_validator(email, password, phone, postal):
    """Validates user data"""
    if not validate_email(email):
        raise Exception('Invalid email')
    elif not check_password(password):
        raise Exception('Invalid password')
    elif not validate_phone_number(phone):
        raise Exception('Invalid phone number')
    elif not validate_postal_code(postal):
        raise Exception('Invalid phone number')
    else:
        logging.info('User input is valid.')


def save_data(email, password, phone, postal):
    """Save data to CSV file"""
    data_file = 'data.csv'
    add_entry = True
    csv_data = []

    if os.path.exists(data_file):
        with open(data_file, mode='a') as _:    #create file
            pass

    with open(data_file, newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row and row[0] == email:
                logging.warning('Email already exist! Overriding data.')
                add_entry = False
                row = email, password, phone, postal
            csv_data.append(row)
        if add_entry:
            csv_data.append([email, password, phone, postal])

    with open(data_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_data)


def main():
    """Main function"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', help='Regex to search',
                        choices=['disable', 'warning', 'info'],
                        default='info')
    args = parser.parse_args()

    if args.verbose == 'disable':
        logging.getLogger().setLevel(logging.CRITICAL)
    elif args.verbose == 'warning':
        logging.getLogger().setLevel(logging.WARNING)
    else:
        logging.getLogger().setLevel(logging.INFO)

    email = input("Enter email:")
    password = input("Enter password:")
    phone = input("Enter phone number:")
    postal = input("Enter postal code:")

    try:
        combined_validator(email, password, phone, postal)
        save_data(email, password, phone, postal)
    except Exception as exp:
        logging.warning('Exception: %s', exp)


if __name__ == "__main__":
    main()
