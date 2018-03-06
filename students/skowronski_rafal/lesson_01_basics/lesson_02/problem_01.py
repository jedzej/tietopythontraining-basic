# Solves problem 01 - Last digit of an integer


def print_last_integer_digit():
    number = int(input('Enter integer number: '))

    print('\nLast digit is {0}'.format(number % 10))

if __name__ == '__main__':
    print_last_integer_digit()
