import re


def main():
    print(is_postal_valid("00-999"))
    print(is_postal_valid("12345"))


def is_postal_valid(postal):
    regex_postal_code_validator = re.compile(r'^\d{2}-\d{3}$')

    return bool(regex_postal_code_validator.match(postal))


if __name__ == '__main__':
    main()
