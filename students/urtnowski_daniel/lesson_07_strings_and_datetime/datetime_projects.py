#!/usr/bin/env python3

"""
datetime_projects.py: practice projects related to date and time: "Date
printer", "Timestamp to date", "Date calculator" and "Delta time calculator"
from:
Lesson 7 - Manipulating strings + datetime formatting
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import datetime
import time


def format_date(date):
    """
    This function  converts received date to human-readable format.
    :param datetime.datetime or datetime.date date: the date to be formatted
    :return string: formatted date
    """
    if type(date) is datetime.date:
        format_str = '%d.%m.%Y r.'
    else:
        format_str = '%H:%M %d.%m.%Y'

    date_str = '{:{fs}}'.format(date, fs=format_str)

    return date_str


def date_printer():
    """
    This function displays current date in human-readable format
    """
    curr_date = datetime.date.today()

    print(format_date(curr_date))


def timestamp_to_date(timestamp=None):
    """
    This function converts unix timestamp to human-readable date format
    :param timestamp: unix timestamp
    :return: string with formatted date
    """
    if timestamp is None:
        timestamp = time.time()

    date = datetime.date.fromtimestamp(timestamp)

    return format_date(date)


def date_calculator(years, days, hours, minutes):
    """
    This function  adds custom number of years, days, hours and minutes
    to current date and displays the result in human readable format
    :param int years: number of years to be added
    :param int days: number of days to be added
    :param int hours: number of hours to be added
    :param int minutes: number of minutes to be added
    """
    now = datetime.datetime.now()

    modified_dt = datetime.datetime(now.year + years, now.month, now.day,
                                    now.hour, now.minute)
    delta = datetime.timedelta(days=days, hours=hours, minutes=minutes)
    modified_dt += delta

    print(format_date(modified_dt))


def delta_time_calculator(future_date):
    """
    This function calculates time difference in days between current date and
    custom date in the future
    :param datetime.date future_date: a custom future date
    :return int: time difference in days
    """
    now = datetime.date.today()
    delta = future_date - now

    return delta.days


def main():

    # Date printer
    date_printer()

    # Timestamp to date
    print(timestamp_to_date())
    print(timestamp_to_date(0))
    print(timestamp_to_date(1524222847.274608))

    # Date calculator
    date_calculator(5, 32, 25, 61)

    # Delta time calculator
    future_date = datetime.date(2035, 11, 17)
    diff_days = delta_time_calculator(future_date)
    print('Time difference between now and {:%d/%m/%Y} is {} days'.format(
          future_date, diff_days))


if __name__ == '__main__':
    main()
