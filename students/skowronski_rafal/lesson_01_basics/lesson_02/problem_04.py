# Solves problem 04 - Fractional part
from decimal import Decimal


def print_fractional_part():
    number = Decimal(input('Enter float number: '))

    print('\nFractional part is: {0}'.format(number % 1))

if __name__ == '__main__':
    print_fractional_part()
