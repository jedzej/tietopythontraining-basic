import re
import argparse
import sys
import logging
import os
import csv
import shutil


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Parse user base parameters')
    parser.add_argument('-em', '--email',
                        help='email address',
                        required='True',
                        # default='andrzej.barecki@tieto.com'  # uncomment
                        #  if workaround for fast testing.
                        # TODO: finally add unit test
                        )

    parser.add_argument('-ps', '--password',
                        help='strong password',
                        required='True',
                        # default='345678aB'  # uncomment if workaround for
                        # fast testing.
                        # TODO: finally add unit test
                        )

    parser.add_argument('-pn', '--phone_number',
                        help='phone number',
                        required='True',
                        # default='+48-123-456-678'  # uncomment if workaround
                        # for fast testing.
                        # TODO: finally add unit test
                        )

    parser.add_argument('-pc', '--postal',
                        help='regex user definition',
                        required='True',
                        # default='00-999'  # uncomment if workaround for fast
                        # testing
                        )

    parser.add_argument('-vo', '--verbose',
                        help='verbosity level: disabled, warning, info',
                        choices=['disabled', 'warning', 'info'],
                        default='info')
    res = parser.parse_args(args)
    return res.email, res.password, res.phone_number, res.postal, res.verbose


def set_verbosity_level(verbosity_level):
    if verbosity_level == 'disabled':
        logging.getLogger().setLevel(logging.CRITICAL)
    elif verbosity_level == 'warning':
        logging.getLogger().setLevel(logging.WARNING)
    else:
        logging.getLogger().setLevel(logging.INFO)


def is_email_valid(email):
    regex_email_validator = re.compile(r'''(
                [a-zA-Z0-9._%+-]+      # username
                @                      # @ symbol
                [a-zA-Z0-9.-]+         # domain name
                (\.[a-zA-Z]{2,3})      # dot-something
                )''', re.VERBOSE)

    return bool(regex_email_validator.match(email))


def is_strong_password(password):
    result = True
    regex_at_least_eight_char = re.compile(r'.{8}')
    regex_uppercase_char = re.compile(r'.*[A-Z]')
    regex_lowercase_char = re.compile(r'.*[a-z]')
    regex_at_least_one_digit = re.compile(r'.*[0-9]')

    result &= bool(regex_at_least_eight_char.match(password))
    result &= bool(regex_uppercase_char.match(password))
    result &= bool(regex_lowercase_char.match(password))
    result &= bool(regex_at_least_one_digit.match(password))
    return result


def is_phone_number(phone_number):
    regex_phone_number_validator = re.compile(
        r'^(\+\d{1,3}[ -])?'  # country prefix
        r'\d{3}'  # 3 digit
        r'(( |-)?\d{3}){2}$')  # 6 digit
    return bool(regex_phone_number_validator.match(phone_number))


def is_postal_valid(postal):
    regex_postal_code_validator = re.compile(r'^\d{2}-\d{3}$')
    return bool(regex_postal_code_validator.match(postal))


def combined_validator(email, password, phone, postal):
    if not is_email_valid(email):
        logging.warning("Email is incorrect!")
        raise Exception("Invalid email!")
    elif not is_strong_password(password):
        logging.warning("Password is incorrect!")
        raise Exception("Invalid password!")
    elif not is_phone_number(phone):
        logging.warning("Phone number is incorrect!")
        raise Exception("Invalid phone number!")
    elif not is_postal_valid(postal):
        logging.warning("Postal code is incorrect!")
        raise Exception("Invalid postal code!")
    else:
        logging.info("Arguments are correct!")


def save_user_base_to_file(user_base_item):

    if os.path.isfile('user_base.csv'):
        logging.info("File user_base.csv exist!")
        with open('user_base.csv', 'r') as csv_rd_file,\
                open('user_base_temp.csv', 'w', newline='') as csv_wr_file:

            try:
                reader = csv.DictReader(csv_rd_file,
                                        fieldnames=user_base_item.keys())
                writer = csv.DictWriter(csv_wr_file,
                                        fieldnames=user_base_item.keys())
                for row in reader:
                    if row['email'] != user_base_item['email']:
                        writer.writerow(row)
                writer.writerow(user_base_item)

            except Exception as err:
                logging.warning("I/O Exception:{0}".format(err))

            finally:
                csv_rd_file.close()
                csv_wr_file.close()
                shutil.move('user_base_temp.csv', 'user_base.csv')

    else:
        logging.info("File user_base.csv will be created!")
        with open('user_base.csv', 'a', newline='') as csv_file:

            try:
                writer = csv.DictWriter(csv_file,
                                        fieldnames=user_base_item.keys())
                writer.writeheader()
                writer.writerow(user_base_item)

            except Exception as err:
                logging.warning("I/O Exception:{0}".format(err))

            finally:
                csv_file.close()


def main():
    """Parse arguments"""
    email_param, password_param, phone_param, postal_param, verbose_param \
        = parse_args(sys.argv[1:])

    """Set logging configuration"""
    logging.basicConfig(level=logging.DEBUG,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    set_verbosity_level(verbose_param)

    """Logging arguments"""
    logging.info("email param: {0}".format(email_param))
    logging.info("password param: {0}".format(password_param))
    logging.info("phone param: {0}".format(phone_param))
    logging.info("postal param: {0}".format(postal_param))
    logging.info("verbose param: {0}".format(verbose_param))

    """try-catch arguments"""
    try:
        combined_validator(email_param, password_param, phone_param,
                           postal_param)

        user_base = {"email": email_param,
                     "password": password_param,
                     "phone": phone_param,
                     "postal": postal_param}

        save_user_base_to_file(user_base)

    except Exception as err:
        logging.warning("Exception:{0}".format(err))


if __name__ == '__main__':
    main()
