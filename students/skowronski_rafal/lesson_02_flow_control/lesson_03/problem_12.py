# Solves problem 12 - leap year


def _main():
    year_number = int(input('Enter year number: '))

    is_leap_year_number = (year_number % 400 == 0) or \
        (year_number % 4 == 0 and year_number % 100 != 0)

    print('{0}'.format('LEAP' if is_leap_year_number is True else 'COMMON'))


if __name__ == '__main__':
    _main()
