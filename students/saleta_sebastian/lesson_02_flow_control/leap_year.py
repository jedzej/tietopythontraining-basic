def check_if_year_is_leap_or_common():
    year = int(input())

    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        print('LEAP')
    else:
        print('COMMON')


if __name__ == '__main__':
    check_if_year_is_leap_or_common()
