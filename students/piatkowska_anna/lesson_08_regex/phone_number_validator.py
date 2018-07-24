'''
Phone number validator - write phone number validator
that accepts phone numbers in not separated,
space-separated or hypen-separated 9-digit
format with optional country prefix
'''
import re


def validate_number(number):
    phoneRule = re.compile(r'''
    ([+]?\d{2}|\([+]?\d{2}\))?   #country prefix
    (\s|-)?                      #separator
    (   #parts of 3 digits
        \d{3}
        (\s|-)?
        \d{3}
        (\s|-)?
        \d{3}
        |   #parts of 2 digits
        \d{3}
        (\s|-)?
        \d{2}
        (\s|-)?
        \d{2}
        (\s|-)?
        \d{2}
    )
    ''', re.VERBOSE)
    res = phoneRule.findall(number)
    if (res != []):
        if (res[0][2] != ""):
            print(number, "is valid.")
    else:
        print(number, "is invalid.")


if __name__ == "__main__":
    validate_number("123456789")
    validate_number("1234")
    validate_number("123-456-789")
    validate_number("123 456 789")
    validate_number("123 45 67 89")
    validate_number("123-45-67-89")
    validate_number("+48 123 456 789")
    validate_number("(+48)123456789")
    validate_number("(+48)1234567 89")
    validate_number("(+48)1234567")
