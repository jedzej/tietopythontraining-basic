from datetime import datetime
from datetime import timedelta

'''
Date calculator - write a script that
adds custom number of years,
days and hours and minutes to current date
and displays the result in human readable format
'''


def calculate_date(years, days, hours, minutes):
    days += years * 365
    return datetime.now() + timedelta(days=days, hours=hours, minutes=minutes)


print(calculate_date(0, 1, 0, 0))
