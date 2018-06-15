import re
import csv
import argparse
import logging
import os


def get_arguments():

    user_data = {}

    parser = argparse.ArgumentParser(description='User base')

    parser.add_argument('-v', action='store',
                        dest='verbose', help='Verbose level - disabled, warning, info',
                        choices=['disabled', 'warning', 'info'],
                        default='disabled')

    parser.add_argument('-e', '--email', action='store',
                        dest="email", required=True,
                        help='Address email')

    parser.add_argument('-p', '--password', action='store',
                        dest="password", required=True,
                        help='Password')

    parser.add_argument('-pn', '--phone', action='store',
                        dest="phone", required=True,
                        help='Phone number')

    parser.add_argument('-pc', '--postalcode', action='store',
                        dest="code", required=True,
                        help='Postal code')

    args = parser.parse_args()

    lvl = args.verbose
    user_data['email'] = args.email
    user_data['password'] = args.password
    user_data['phone_number'] = args.phone
    user_data['postal_code'] = args.code

    return user_data, lvl


def combined_validator(data):
    logging.info('Email validation')
    regex = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+.[a-zA-Z0-9]{2,3}')
    mo = regex.search(data['email'])
    if mo is None:
        raise Exception('Wrong email address')

    logging.info('Password validation')
    regex = re.compile(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?\d)(?=.*?\W).{8,}')
    mo = regex.search(data['password'])
    if mo is None:
        raise Exception('Password too weak')

    logging.info('Phone number validation')
    regex = re.compile(r'(\d{2}[- ]?)?((\d{3})[- ]?(\d{3})[- ]?(\d{3}))')
    mo = regex.search(data['phone_number'])
    if mo is None:
        raise Exception('Wrong phone number')

    logging.info('Postal ccde validation')
    regex = re.compile(r'\d{2}-\d{3}')
    mo = regex.search(data['postal_code'])
    if mo is None:
        raise Exception('Wrong post code')


def verbose_output(level='default'):
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

    if level == 'disabled':
        logging.disable(logging.CRITICAL)
    elif level == 'warning':
        logging.getLogger().setLevel(logging.WARNING)
    else:
        logging.getLogger().setLevel(logging.INFO)


def write_to_file(data):
    flag = 0
    logging.info('Write to file')
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        list_of_rows = list(reader)
        for i in range(len(list_of_rows)):
            if list_of_rows[i][0] == data['email']:
                logging.info('Change values of existing email record')
                for x in range(len(list_of_rows[i])):
                    list_of_rows[i][x] = list(data.values())[x]
                    flag = 1
                break

        if flag == 0:
            logging.info('Adding new record to list')
            list_of_rows.append([data['email'], data['password'],
                                 data['phone_number'], data['postal_code']])

    with open('test.csv', 'w') as myfile:
        for list_row in list_of_rows:
            for i, item in enumerate(list_row):
                if i == 0:
                    myfile.write(item)
                else:
                    myfile.write(',' + item)
            myfile.write('\n')

    os.remove('data.csv')
    os.rename('test.csv', 'data.csv')
    logging.info('Done')


user, verbose_level = get_arguments()
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
verbose_output(level=verbose_level)
combined_validator(user)
write_to_file(user)
