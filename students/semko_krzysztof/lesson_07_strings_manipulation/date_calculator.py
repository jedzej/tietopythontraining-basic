"""
Date calculator - write a script that adds custom
number of years, days and hours and minutes to current
date and displays the result in human readable format
"""
from datetime import datetime
from time import time

MIN = 60
HOUR = MIN * 60
DAY = HOUR * 24
YEAR = DAY * 365


def main():
    print("Please input years to add:")
    years = int(input())
    print("Please input days to add:")
    days = int(input())
    print("Please input hours to add:")
    hours = int(input())
    print("Please input minutes to add:")
    minutes = int(input())

    now = time()
    # Assumption: year is a non-leap, 365 days
    to_add = minutes * MIN + hours * HOUR + days * DAY \
        + years * YEAR

    ts = now + to_add
    print(datetime.fromtimestamp(ts).strftime('%Y.%m.%d %H:%M'))


if __name__ == '__main__':
    main()
