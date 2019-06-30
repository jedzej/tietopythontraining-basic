import argparse
import csv
import os
import re
import logging

logging.getLogger().setLevel(logging.INFO)


def email_validator(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)''*@[a-z0-9-]+'
                     '(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match is None:
        return False
    else:
        logging.info("Email is OK")
        return True


def phone_validator(phone_number):

    phone = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
    if phone.match(phone_number) is not None:
        logging.info("Number is OK")
        return True
    else:
        return False


def post_code_validator(post_code):
    code = re.compile(r'^\d{2}-\d{3}$')
    if code.match(post_code) is not None:
        logging.info("Post code is OK")
        return True
    else:
        return False


parser = argparse.ArgumentParser(description='data')

parser.add_argument('-e', '--email', action='store',
                    dest="email", required=True,
                    help='Address email')

parser.add_argument('-pn', '--phone', action='store',
                    dest="phone", required=True,
                    help='Phone number')

parser.add_argument('-pc', '--postalcode', action='store',
                    dest="code", required=True,
                    help='Postal code')

args = parser.parse_args()

if not email_validator(args.email):
    raise Exception("Email is wrong")

if not phone_validator(args.phone):
    raise Exception("Wrong format")

if not post_code_validator(args.code):
    raise Exception("Invalid syntax")

logging.info('Write to file')
csv_file = 'data.csv'

user_data_list = []
user_record_exist = False

if not os.path.exists(csv_file):
    open(csv_file, 'a')

with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == args.email:
            row = args.email, args.phone, args.code
            user_record_exist = True
            logging.warning('This record dalready exists')
        user_data_list.append(row)
    if not user_record_exist:
        user_data_list.append([args.email, args.phone, args.code])

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(user_data_list)
