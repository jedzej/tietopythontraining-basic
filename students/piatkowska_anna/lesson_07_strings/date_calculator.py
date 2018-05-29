'''
Date calculator - write a script that adds custom number of years,
days and hours and minutes to current date and displays
the result in human readable format
'''

from datetime import datetime
import calendar  # calendar.monthrange


def add_date(y, d, h, m):
    date = datetime.utcnow()
    print('current time: {:%Y %B %d %H:%M:%S}'.format(date))
    new_year = date.year + y
    new_month = date.month
    new_day = date.day + d
    new_hours = date.hour + h
    new_minutes = date.minute + m
    while new_minutes > 60:
        new_minutes -= 60
        new_hours += 1
    while new_hours > 24:
        new_hours -= 24
        new_day += 1
    days_in_month = calendar.monthrange(new_year, new_month)[1]
    while new_day > days_in_month:
        new_day -= days_in_month
        if new_month < 12:
            new_month += 1
        else:
            new_month = 1
            new_year += 1
        days_in_month = calendar.monthrange(new_year, new_month)[1]
    res = datetime(new_year, new_month, new_day, new_hours,
                   new_minutes, date.second)
    return '{:%Y %B %d %H:%M:%S}'.format(res)


if __name__ == "__main__":
    print("")
    print("Adding an year, a day, an hour, minutes to current date: ")
    print(add_date(1, 1, 1, 1))
    print("add_date(100, 1, 1, 20)")
    print(add_date(100, 1, 1, 20))
    print("add_date(10, 100, 100, 200)")
    print(add_date(10, 100, 100, 200))
