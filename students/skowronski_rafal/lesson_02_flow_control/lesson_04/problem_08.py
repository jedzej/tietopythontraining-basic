# Solves problem 07 - Adding factorials


def _main():
    number = int(input('Enter an integer number (n): '))

    last_factorial = 1
    sum_of_factorials = last_factorial
    for i in range(2, number + 1):
        last_factorial *= i
        sum_of_factorials += last_factorial

    print('\nSum of factorials = {0}'.format(sum_of_factorials))


if __name__ == '__main__':
    _main()
