import re


def validate_email(email):
    if len(email) > 254:
        return False

    mail_pattern = re.compile(r'(^[a-zA-Z]'
                              '[a-zA-Z0-9.!#$%&\'*+\-/=?^_`{|}~]+'
                              '@'
                              '[a-zA-Z0-9\-]+'
                              '\.'
                              '[a-zA-Z0-9/-]+'
                              '[a-zA-Z0-9]$)')
    return mail_pattern.match(email)


def validate_number(number):
    number_pattern = re.compile(r'^(\+)?((\d){2})?'
                                '(' '|\-)?((\d){3})'
                                '(' '|\-)?((\d){3})'
                                '(' '|\-)?((\d){3})$')
    return number_pattern.match(number)


def validate_postal_code(code):
    if len(code) != 6:
        return False
    postal_pattern = re.compile(r"^[0-9]{2}-[0-9]{3}$")
    return postal_pattern.match(code)


def validate_password(password):
    check_space = re.compile(r" *")
    password_no_white_space = check_space.sub('', password)
    if password != password_no_white_space:
        print("There shouldn't be any white spaces in the password")
        return False

    if len(password) < 8:
        print("Password is too short")
        return False

    if (re.compile(r".*[a-z]").match(password) and
            re.compile(r".*[A-Z]").match(password) and
            re.compile(r".*[0-9]").match(password)):
        return True
    return False
