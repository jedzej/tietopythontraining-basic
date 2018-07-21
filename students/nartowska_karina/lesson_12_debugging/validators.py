import re


def email_validator(email):
    r_email = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    if r_email.match(email):
        return 1


def phone_number_validator(number):
    r_number = re.compile(r'^(\+\d{1,3} ?)?\d{3}([ -]?\d{3}){2}$')
    if r_number.match(number):
        return 1


def postal_code_validator(code):
    r_code = re.compile(r'^\d{2}-\d{3}$')
    if r_code.match(code):
        return 1


def strong_password_detection(password):
    r_password = re.compile(r'^(.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')
    if r_password.match(password):
        return 1
