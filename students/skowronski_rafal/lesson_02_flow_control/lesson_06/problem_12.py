# Solves problem 12 - The second maximum


def _main():
    print('Enter sequence of integers:')

    maximum = second_maximum = 0
    while True:
        number = int(input())

        if number > maximum:
            second_maximum = maximum
            maximum = number
        elif number > second_maximum:
            second_maximum = number

        if (number == 0):
            break

    print('The second maximum of the sequence: {0}'.format(second_maximum))


if __name__ == '__main__':
    _main()
