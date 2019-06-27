import sys
import regex_validator
import logging
import csv
import argparse

logging.basicConfig(format=' %(asctime)s - %(levelname)s- %(message)s')


def combined_validator(email_addr, phone_nr, postal_code, passwd):
    if not regex_validator.email_validator(email_addr):
        raise Exception("Incorrect email")
    if not regex_validator.phone_number_validator(phone_nr):
        raise Exception("Incorrect phone number")
    if not regex_validator.postal_code_validator(postal_code):
        raise Exception("Incorrect postal code")
    if not regex_validator.pass_checker(passwd):
        raise Exception("Strong password required")


def set_verbose_level(verbose_level):
    logger = logging.getLogger()
    if verbose_level == "info":
        logger.setLevel(logging.INFO)
    elif verbose_level == "warning":
        logger.setLevel(logging.WARNING)
    else:
        logger.disabled = True


def check_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email",
                        help="email",
                        required=True)
    parser.add_argument("-p", "--password",
                        help="password",
                        required=True)
    parser.add_argument("-n", "--number",
                        help="phone number",
                        required=True)
    parser.add_argument("-c", "--code",
                        help="postal code",
                        required=True)
    parser.add_argument("-v", "--verbose",
                        help="verbose level",
                        choices=['disabled', 'warning', 'info'],
                        default="warning")
    res = parser.parse_args(args)
    return res.email, res.password, res.number, res.code, res.verbose


email, password, number, code, verbose = check_args(sys.argv[1:])
user_data = {"email": email, "password": password, "number": number,
             "code": code}


def write_csv(write_file, read_file):
    with open(write_file, 'a') as csv_write_file, open(read_file,
                                                       'r') as csv_read_file:
        fieldnames = ['email', 'password', 'number', 'code']
        reader = csv.DictReader(csv_read_file, fieldnames=fieldnames)
        writer = csv.DictWriter(csv_write_file, fieldnames=fieldnames)
        email_exists = False
        for i in reader:
            logging.info("Data stored in file: {}".format(i))
            if i['email'] == user_data['email']:
                logging.info("email {} exists. Replacing user's data".format(
                    i['email']))
                email_exists = True
        if not email_exists:
            writer.writerow(user_data)
            logging.info("User doesn't exists, adding new user's data.")
            logging.info("Added user data: {}".format(user_data))


if __name__ == '__main__':
    level = verbose
    set_verbose_level(level)
    combined_validator(email, number, code, password)
    write_csv("test.csv", "test.csv")