# Solves problem 07 - The number of zeros


def _main():
    numbers_number = int(input('Enter a number of numbers (N): '))

    number_of_zeros = 0
    for _ in range(numbers_number):
        number = int(input('Enter integer number : '))
        number_of_zeros = number_of_zeros + 1 \
            if number == 0 else number_of_zeros

    print('\nNumber of zeros = {0}'.format(number_of_zeros))


if __name__ == '__main__':
    _main()
