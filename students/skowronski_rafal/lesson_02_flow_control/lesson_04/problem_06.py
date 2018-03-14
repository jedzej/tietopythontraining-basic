# Solves problem 06 - Factorial


def _main():
    number = int(input('Enter an integer number (n): '))

    factorial = 1
    for i in range(2, number + 1):
        factorial = factorial * i

    print('\nn! = {0}'.format(factorial))


if __name__ == '__main__':
    _main()
