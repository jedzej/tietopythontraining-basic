import re


def email_validator(email):
    regex = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    return regex.match(email) is not None


def main():
    test = "test@test.pl"
    print(test, "is valid email: ", email_validator(test))


if __name__ == '__main__':
    main()
