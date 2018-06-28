from random import randint
from datetime import datetime, timedelta


def print_shift_date(years, days, hours, minutes):
    today_date = datetime.now()
    output_date = datetime(today_date.year + years,
                           today_date.month,
                           today_date.day) + timedelta(days=days,
                                                       hours=hours,
                                                       minutes=minutes)

    print('SHIFT DATE: {:{dfmt} {tfmt}}'
          .format(output_date, dfmt='%d-%m-%Y', tfmt='%H:%M:%S'))


def main():
    print_shift_date(randint(0, 100), randint(0, 12),
                     randint(0, 24), randint(0, 60))


if __name__ == '__main__':
    main()
