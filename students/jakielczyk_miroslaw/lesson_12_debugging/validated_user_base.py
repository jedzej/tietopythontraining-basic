import re
import argparse
import sys
import csv
import logging


def collect_arguments(args=None):
    parser = argparse.ArgumentParser(description='Script to learn basic arg-parse')

    parser.add_argument('-e', '--email',
                        help='enter email address',
                        default='miroslaw.jakielczyk@tieto.com')

    parser.add_argument('-pw', '--password',
                        help='enter password',
                        default='ABCD1234efg')

    parser.add_argument('-pn', '--phone_number',
                        help='enter phone number',
                        default='668168240')

    parser.add_argument('-pc', '--postal_code',
                        help='enter postal code',
                        default='64-104')

    parser.add_argument('-vo', '--verbose_output',
                        help='logging level, possible values: disabled, warning, info',
                        default='info')

    results = parser.parse_args(args)

    return (results.email, results.password, results.phone_number,
            results.postal_code, results.verbose_output)


def validate_email_address(email_address):
    email_regex = re.compile(r'''(
                    [a-zA-Z0-9._%+-]+      # username
                    @                      # @ symbol
                    [a-zA-Z0-9.-]+         # domain name
                    (\.[a-zA-Z]{2,3})      # dot-something
                    )''', re.VERBOSE)

    email_match = email_regex.search(email_address)

    if email_match is not None:
        logging.info('Email address is valid: ' + email_match.group(0))
    else:
        logging.error('Given email is incorrect, further proceeding is skipped')
        raise Exception('Given email address is incorrect')


def validate_phone_number(phone_number):
    phone_num_regex = re.compile(r'''(
                        ((^\+(\d){2,3})?\s\d{3}\s\d{3}\s\d{3}$)       # space separated
                        |(^(\+(\d){2,3})?\d{9}$)                       # no separated
                        |(^(\+(\d){2,3})?-?\d{3}-?\d{3}-?\d{3}$)      # hyphen-separated
                        )''', re.VERBOSE)

    phone_number_match = phone_num_regex.search(phone_number)

    if phone_number_match is not None:
        logging.info('Phone number is valid: ' + phone_number_match.group(0))
    else:
        logging.error('Given phone number is incorrect, further proceeding is skipped')
        raise Exception('Given phone number is incorrect')


def validate_postal_code(postal_code):
    postal_code_regex = re.compile(r'^\d{2}-\d{3}$')
    postal_code_match = postal_code_regex.search(postal_code)

    if postal_code_match is not None:
        logging.info('Postal code is valid: ' + postal_code_match.group())
    else:
        logging.error('Given postal code is incorrect, further proceeding is skipped')
        raise Exception('Postal code is incorrect')


def validate_strong_password(password):
    strong_password = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)([\w!@#$%^&*(),.?]{8,})$')
    if strong_password.search(password) is not None:
        logging.info('Password is valid: ' + password)
    else:
        logging.error('Given password is incorrect, further proceeding is skipped')
        raise Exception('Password is incorrect')


def combined_validator(email_address, password, phone_number, postal_code):
    try:
        validate_email_address(email_address)
        validate_strong_password(password)
        validate_phone_number(phone_number)
        validate_postal_code(postal_code)
        update_user_database('user_data.csv', email_address, password, phone_number, postal_code)
    except Exception as err:
        print('An exception happened: ' + str(err))


def update_user_database(csv_file_name, email, password, phone_number, postal_code):
    user_data_list = []
    user_record_exist = False
    with open(csv_file_name, newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] == email:
                row = email, password, phone_number, postal_code
                user_record_exist = True
                logging.warning('This email exist in database, will be altered')
            user_data_list.append(row)
        if not user_record_exist:
            user_data_list.append([email, password, phone_number, postal_code])
    with open(csv_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(user_data_list)


def main():
    logging_level = {'disabled': logging.CRITICAL, 'warning': logging.INFO, 'info': logging.DEBUG}
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

    email_address, phone_number, postal_code, password, verbose_output = collect_arguments(sys.argv[1:])

    if verbose_output in logging_level:
        logging.disable(logging_level[verbose_output])
    else:
        logging.disable(logging.CRITICAL)

    combined_validator(email_address, phone_number, postal_code, password)


if __name__ == "__main__":
    main()
