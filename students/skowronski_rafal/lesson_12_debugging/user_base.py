import regex
import logging
import bcrypt
import csv
import io
import traceback
import getpass


def ensure_valid_email(email):
    if not regex.is_valid_email_address(email):
        raise ValueError('Invalid email address format')


def ensure_valid_password(password):
    if not regex.is_password_strong(password):
        raise ValueError('Password is not strong enough')


def ensure_valid_phone_number(phone_number):
    if not regex.is_valid_mobile_phone_number(phone_number):
        raise ValueError('Invalid phone number format')


def ensure_valid_postal_code(postal_code):
    if not regex.is_valid_postal_code(postal_code):
        raise ValueError('Invalid postal code format')


def ensure_valid_parameters(parameters):
    email, password, phone_number, postal_code = parameters
    try:
        ensure_valid_email(email)
        ensure_valid_password(password)
        ensure_valid_phone_number(phone_number)
        ensure_valid_postal_code(postal_code)
    except ValueError:
        logging.critical(traceback.format_exc)
        raise


def read_input_parameters():
    email = input('Enter email address: ')
    password = getpass.getpass(prompt='Enter password: ')
    phone_number = input('Enter phone number: ')
    postal_code = input('Enter postal code: ')

    return (email, password, phone_number, postal_code)


def get_arguments_row(arguments):
    email, password, phone_number, postal_code = parameters

    return (email,
            bcrypt.hashpw(bytes(password, encoding='utf-8'),
                          bcrypt.gensalt()),
            phone_number,
            postal_code)


def save_csv(arguments):
    with io.StringIO() as tmp_stream:

        with open('database.csv',
                  mode='a+',
                  newline='',
                  encoding='utf-8') as csv_stream:
            altered = False
            csv_stream.seek(0)
            reader = csv.reader(csv_stream)
            writer = csv.writer(tmp_stream)
            for row in reader:
                if row[0] == arguments[0]:
                    writer.writerow(get_arguments_row(arguments))
                    logging.info('Replaced entry for user: {0}'
                                 .format(arguments[0]))
                    altered = True
                else:
                    writer.writerow(row)
            if not altered:
                writer.writerow(get_arguments_row(arguments))
                logging.info('Added entry for user: {0}'
                             .format(arguments[0]))

        with open('database.csv',
                  mode='w',
                  newline='',
                  encoding='utf-8') as csv_stream:
            tmp_stream.seek(0)
            csv_stream.write(tmp_stream.read())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s - %(asctime)s - %(message)s')

    parameters = read_input_parameters()
    ensure_valid_parameters(parameters)
    save_csv(parameters)
