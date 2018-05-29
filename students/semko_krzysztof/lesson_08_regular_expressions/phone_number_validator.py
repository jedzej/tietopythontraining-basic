"""
Phone number validator - write phone number validator that
accepts phone numbers in not separated, space-separated
or hypen-separated 9-digit format with optional
country prefix
"""
import re


def check_number(number):
    number_pattern = re.compile(r'^(\+)?((\d){2})?'
                                '(' '|\-)?((\d){3})'
                                '(' '|\-)?((\d){3})'
                                '(' '|\-)?((\d){3})$')
    return number_pattern.match(number)


def main():
    print("Please input phone number:")
    if check_number(input()):
        print("This is a correct phone number")
    else:
        print("This is not a correct phone number")


if __name__ == '__main__':
    main()
