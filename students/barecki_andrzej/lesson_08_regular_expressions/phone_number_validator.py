import re

"""Phone number validator - accepts phone numbers in not separated,
 space-separated or hypen-separated 9-digit format with optional
 country prefix"""


def main():
    pn1 = "+48-123-456-678"
    pn2 = "+48123456678"
    pn3 = "+48-123456678"
    pn4 = "+48 123456678"
    pn5 = "48-123-456-678"
    pn6 = "-123-456-678"
    pn7 = "123-456-678"
    pn8 = "123 456 678"
    pn9 = "123456678"

    print(pn1 + " is phone number: {0}".format(is_phone_number(pn1)))
    print(pn2 + " is phone number: {0}".format(is_phone_number(pn2)))
    print(pn3 + " is phone number: {0}".format(is_phone_number(pn3)))
    print(pn4 + " is phone number: {0}".format(is_phone_number(pn4)))
    print(pn5 + " is phone number: {0}".format(is_phone_number(pn5)))
    print(pn6 + " is phone number: {0}".format(is_phone_number(pn6)))
    print(pn7 + " is phone number: {0}".format(is_phone_number(pn7)))
    print(pn8 + " is phone number: {0}".format(is_phone_number(pn8)))
    print(pn9 + " is phone number: {0}".format(is_phone_number(pn9)))


def is_phone_number(phone_number):
    regex_phone_number_validator = re.compile(
        r'^(\+\d{1,3}[ -])?'    # country prefix
        r'\d{3}'                # 3 digit
        r'(( |-)?\d{3}){2}$')   # 6 digit

    return bool(regex_phone_number_validator.match(phone_number))


if __name__ == '__main__':
    main()
