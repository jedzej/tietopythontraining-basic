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

    print("{0:15s} is phone number: {1}".format(pn1, is_phone_number(pn1)))
    print("{0:15s} is phone number: {1}".format(pn2, is_phone_number(pn2)))
    print("{0:15s} is phone number: {1}".format(pn3, is_phone_number(pn3)))
    print("{0:15s} is phone number: {1}".format(pn4, is_phone_number(pn4)))
    print("{0:15s} is phone number: {1}".format(pn5, is_phone_number(pn5)))
    print("{0:15s} is phone number: {1}".format(pn6, is_phone_number(pn6)))
    print("{0:15s} is phone number: {1}".format(pn7, is_phone_number(pn7)))
    print("{0:15s} is phone number: {1}".format(pn8, is_phone_number(pn8)))
    print("{0:15s} is phone number: {1}".format(pn9, is_phone_number(pn9)))


def is_phone_number(phone_number):
    regex_phone_number_validator = re.compile(
        r'^(\+\d{1,3}[ -])?'    # country prefix
        r'\d{3}'                # 3 digit
        r'(( |-)?\d{3}){2}$')   # 6 digit

    return bool(regex_phone_number_validator.match(phone_number))


if __name__ == '__main__':
    main()
