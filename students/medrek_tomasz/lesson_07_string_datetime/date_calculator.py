#!/usr/bin/env python3


from datetime import timedelta, datetime


def date_calculator(given_date, added_years, timedelta_args):
    if added_years:
        if added_years < 0:
            sign = -1
            start = given_date.year + added_years
            stop = given_date.year
        else:
            sign = 1
            start = given_date.year
            stop = given_date.year + added_years

        timedelta_args.setdefault('days', 0)
        for year in range(start, stop):
            if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                timedelta_args['days'] += 366 * sign
            else:
                timedelta_args['days'] += 365 * sign

    return given_date + timedelta(**timedelta_args)


def main():
    date_variables = ['years', 'weeks', 'days', 'hours', 'minutes', 'seconds']
    change_date_data = {}

    print("\nWelcome to date calculator!\n".center(81, '+'))
    print("Please fill following variables you want to add to current date,\n"
          "default number is 0, so you can press enter to quick skip.\n")

    for item in date_variables:
        try:
            input_number = int(input("number of {}:\n".format(item)))
        except ValueError:
            input_number = 0

        change_date_data.update({item: input_number})

    result_date = date_calculator(datetime.now(),
                                  change_date_data.pop('years'),
                                  change_date_data)
    print('Result is:\n{:{dfmt} {tfmt}}'.format(
        result_date, dfmt='%Y-%m-%d', tfmt='%H:%M:%S'))


if __name__ == "__main__":
    main()
