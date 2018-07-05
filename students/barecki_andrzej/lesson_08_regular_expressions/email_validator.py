import re


def main():
    print(is_email_valid("a@wp.pl"))
    print(is_email_valid("a@wp"))


def is_email_valid(mail):
    regex_email_validator = re.compile(r'''(
                [a-zA-Z0-9._%+-]+      # username
                @                      # @ symbol
                [a-zA-Z0-9.-]+         # domain name
                (\.[a-zA-Z]{2,3})      # dot-something
                )''', re.VERBOSE)

    return bool(regex_email_validator.match(mail))


if __name__ == '__main__':
    main()
