import re


def main():
    password_example1 = "345678aB"
    print(is_strong_password(password_example1))


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


if __name__ == '__main__':
    main()
