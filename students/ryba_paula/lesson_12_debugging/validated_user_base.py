import logging
import argparse
import sys
import shutil
import validators
import csv
import os.path

logging.basicConfig(format=' %(asctime)s - %(levelname)s - %(message)s')


def arg_input(args):
    parser = argparse.ArgumentParser(description="This script saves validated "
                                                 "user info to .csv file")
    parser.add_argument('-e', '--email', help='email address',
                        required=True)
    parser.add_argument('-n', '--number', help='phone number',
                        required=True)
    parser.add_argument('-c', '--code', help='postal code',
                        required=True)
    parser.add_argument('-p', '--password', help='strong password',
                        required=True)
    parser.add_argument('-v', '--verbose',
                        help='log level',
                        choices=['disabled', 'warning', 'info'], required=True)
    res = parser.parse_args(args)
    return res.email, res.number, res.code, res.password, res.verbose


email, number, code, password, log_level = arg_input(sys.argv[1:])
data = {"email": email, "number": number, "code": code, "password": password}


def set_log_level(lvl):
    logger = logging.getLogger()
    if lvl == 'disabled':
        return logging.disable(logging.CRITICAL)
    elif lvl == 'warning':
        return logger.setLevel(logging.WARNING)
    elif lvl == 'info':
        return logger.setLevel(logging.INFO)


def combined_validator(mail, nr, code, passwd):
    if not validators.email_validator(mail):
        raise Exception("Email is not valid")
    elif not validators.phone_validator(nr):
        raise Exception("Phone number is not valid")
    elif not validators.postal_validator(code):
        raise Exception("Postal code is not valid")
    elif not validators.password_check(passwd):
        raise Exception("Password is not valid")


def write_to_file(dictionary):
    if os.path.isfile('data.csv') or os.path.isfile('tmp.csv'):
        logging.info("File exists")
        with open('data.csv', 'r') as infile, open('tmp.csv', 'w') as outfile:
            reader = csv.DictReader(infile, fieldnames=dictionary.keys())
            writer = csv.DictWriter(outfile, fieldnames=dictionary.keys())
            email_exists = False
            for i in reader:
                logging.info("Data in file: {}".format(i))
                if i['email'] == dictionary['email']:
                    logging.info("{} exists, replacing".format(i['email']))
                    i = dictionary
                    email_exists = True
                writer.writerow(i)
            if not email_exists:
                writer.writerow(dictionary)
                logging.info("User does not exist, adding")

    else:
        logging.warning("File does not exist, creating...")
        with open('tmp.csv', 'a') as infile:
            writer = csv.DictWriter(infile, fieldnames=dictionary.keys())
            writer.writerow(dictionary)
            logging.info("User info saved")

        open('data.csv', 'a')

    shutil.move('tmp.csv', 'data.csv')


def main():
    try:
        set_log_level(log_level)
        combined_validator(email, number, code, password)
        write_to_file(data)
        logging.info("Done")
    except Exception as err:
        logging.warning("An exception happened: {}".format(err))


if __name__ == '__main__':
    main()
