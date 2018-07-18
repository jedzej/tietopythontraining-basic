import re


def email_validator(some_email):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    result = email_regex.match(some_email)
    if result is None:
        return False
    else:
        return True


def phone_number_validator(some_number):
    phone_regex = re.compile(r"^\d{3}[- ]?\d{3}[- ]?\d{3}$")
    if phone_regex.match(some_number) is None:
        return False
    else:
        return True


def postal_code_validator(some_postal_code):
    postal_code_regex = re.compile(r"^\d\d-\d\d\d$")
    if postal_code_regex.match(some_postal_code) is None:
        return False
    else:
        return True


def pass_checker(some_password):
    if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$',
                some_password) is None:
        return False
    else:
        return True
