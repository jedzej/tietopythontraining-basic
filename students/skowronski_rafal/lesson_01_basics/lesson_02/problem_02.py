# Solves problem 02 - Tens digit


def print_last_integer_digit():
    number = int(input('Enter integer number: '))

    print('\nTens digit is: {0}'.format((number % 100) // 10))

if __name__ == '__main__':
    print_last_integer_digit()
