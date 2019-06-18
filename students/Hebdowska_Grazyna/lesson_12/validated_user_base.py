import re
import argparse
import sys
import logging


LOGGING = {"debug": logging.DEBUG,
           "warning": logging.WARNING,
           "info": logging.INFO}


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Give searched regex: ')
    parser.add_argument('-e', '--email',
                        help='"Give email: "',
                        default='llmjk@bo.as')
    parser.add_argument('-p', '--password',
                        help='"Give pasword: "',
                        default='7htjna12maAla')
    parser.add_argument('-n', '--number',
                        help='"Give phone number: "',
                        default='123456789')
    parser.add_argument('-c', '--code',
                        help='"Give postal code: "',
                        default='55-120')

    parser.add_argument('-l', '--logger',
                        help='Give logger level: disabled, warning or info',
                        default='debug')

    results = parser.parse_args(args)
    return (results.email, results.password,
            results.number, results.code, results.logger)


def email_validator(email):
    s = r'''((\w{1,})(\.{1})*(\w{1,})*(\w[@]{1})(\w{1,})(\.{1})(\w{2,3}))'''
    re_mail = re.compile(s)
    mo = re_mail.search(email)

    if mo is not None:
        if mo.group() == email:
            return True
    else:
        return False


def phone_validator(phone_number):
    s = r'''(\+\d{2})?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})'''
    re_number = re.compile(s)
    mo = re_number.search(phone_number)

    if mo is not None:
        if mo.group() == phone_number:
            return True
        else:
            return False
    else:
        return False


def postal_code_validator(code_number):
    re_number = re.compile(r'''((\d{2})(\s|-|\.)(\d{3}))''')
    mo = re_number.search(code_number)
    if mo is not None:
        return True
    else:
        return False


def check_strong(password):
    re_number1 = re.compile(r'''((\w[a-z]{1,})+)''')
    re_number2 = re.compile(r'''((\w[A-Z]{1,})+)''')
    re_number3 = re.compile(r'''((\d{1,})+)''')
    mo1 = re_number1.search(password)
    mo2 = re_number2.search(password)
    mo3 = re_number3.search(password)
    if mo1 is None:
        return False
    elif mo2 is None:
        return False
    elif mo3 is None:
        return False
    else:
        return True


def check_password(password):
    if len(password) < 8:
        return False
    else:
        return check_strong(password)


def is_email(file, email):
    saved_data = file.read().split('\n')
    logging.info("Number of elements: " + str(len(saved_data)))
    logging.info(saved_data)
    for element in range(len(saved_data)):
        if email in saved_data[element]:
            return element


def save_to_csv(data, email):
    logging.info("data " + data)
    try:
        file = open('data.csv', 'r')
        logging.info("open file")
        element = is_email(file, email)
        file.close()
        file = open('data.csv', 'r')
        saved_data = file.read().split('\n')
        logging.info("s: " + str(saved_data))
        if element is not None:
            logging.info("email was found")
            logging.info("Number of elements: " + str(len(saved_data)))
            saved_data[element] = data
        else:
            logging.info("email added")
            saved_data.append(data)
        logging.info("new number: " + str(len(saved_data)))
        logging.info(saved_data)
        file.close()
        file = open('data.csv', 'w')
        for element in saved_data:
            file.write(element + '\n')

    except:
        logging.info("exception")
        file = open('data.csv', 'w')
        file.write(data)
    file.close()


def checking(fun, data, parameter):
    if fun is True:
        logging.info('ok')
        data += " " + parameter
        logging.info("checking data :" + data)
        return data
    else:
        return 'verification failed'


def validator():
    email, password, phone_number, postal_code, log_level = \
        check_arg(sys.argv[1:])
    logging.basicConfig(filename='myProgramLog.txt', level=LOGGING[log_level],
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Start")
    data = ''
    try:
        data = checking(email_validator(email), data, email)
        data = checking(check_password(password), data, password)
        data = checking(postal_code_validator(postal_code), data, postal_code)
        data = checking(phone_validator(phone_number), data, phone_number)
        save_to_csv(data, email)
    except Exception:
        logging.warning("incorrect value")
    logging.info('End of validations')


validator()
