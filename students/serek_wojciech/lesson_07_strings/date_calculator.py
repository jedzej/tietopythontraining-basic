#!/usr/bin/env python3
"""Date printer exercise"""
import datetime
from date_printer import date_printer


def date_calculator(years, days, hours, minutes):
    """Add time parameters to current date and returns new date"""
    now = datetime.datetime.now()
    new_date = datetime.datetime(years + now.year, now.month, now.day,
                                 now.hour, now.minute)

    new_date += datetime.timedelta(days=days, hours=hours, minutes=minutes)
    return date_printer(new_date)


def main():
    """Main function"""
    years = int(input('Years: '))
    days = int(input('Days: '))
    hrs = int(input('Hours: '))
    minutes = int(input('Minutes: '))

    print(date_calculator(years, days, hrs, minutes))


if __name__ == '__main__':
    main()
