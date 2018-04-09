# Solves problem 13 - The number of elements equal to the maximum


def _main():
    print('Enter sequence of integers:')

    maximum = number_of_maximums = 0
    while True:
        number = int(input())

        if number > maximum:
            number_of_maximums = 1
            maximum = number
        elif number == maximum:
            number_of_maximums += 1

        if (number == 0):
            break

    print('The number of elements equal to the maximum: ' +
          '{0}'.format(number_of_maximums))


if __name__ == '__main__':
    _main()
