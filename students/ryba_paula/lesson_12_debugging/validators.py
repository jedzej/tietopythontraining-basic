import re


def email_validator(email):
    regex_email = re.compile(r'(^[a-zA-Z0-9.!#$%&\'*+\-/=?^_`{|}~]+'
                             r'@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    if regex_email.match(email):
        return True
    return False


def phone_validator(number):
    regex_phone = re.compile(r'^(\+\d\d[ -]?)?'
                             '\d{3}(([ -]?\d{3}){2}$|([ -]?\d{2}){3}$)')

    if regex_phone.match(number):
        return True
    return False


def postal_validator(code):
    regex_postal = re.compile(r'^\d{2}-\d{3}$')
    if regex_postal.match(code):
        return True
    return False


def password_check(password):
    if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(.{8,})', password):
        return True
    return False
