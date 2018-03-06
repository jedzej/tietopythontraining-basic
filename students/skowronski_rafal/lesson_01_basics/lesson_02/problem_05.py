# Solves problem 05 - First digit after decimal point
from decimal import Decimal


def print_first_digit_after_decimal_point():
    number = Decimal(input('Enter float number: '))

    first_digit = int((number % 1) * 10)

    print('\nFirst digit after decimal point is: {0}'.format(first_digit))

if __name__ == '__main__':
    print_first_digit_after_decimal_point()
