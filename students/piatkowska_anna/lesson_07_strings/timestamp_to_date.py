'''
Timestamp to date - write a script that converts
unix timestamp to human-readable date format
1526373175 seconds since Jan 01 1970. (UTC)
05/15/2018 @ 8:32am (UTC)
'''
from datetime import datetime


def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def seconds_in_year(year):
    if is_leap(year):
        return 366 * 24 * 60 * 60
    else:
        return 365 * 24 * 60 * 60


def timestamp_to_date1(whole_seconds):
    date = datetime.fromtimestamp(int(whole_seconds))
    return '{:%Y %B %d %H:%M:%S}'.format(date)


def timestamp_to_date2(whole_seconds):
    all = int(whole_seconds)
    year = 1970
    seconds_in_current_year = seconds_in_year(year)
    while all > seconds_in_current_year:
        all = all - seconds_in_current_year
        year += 1
        seconds_in_current_year = seconds_in_year(year)
    day_in_february = 28
    if is_leap(year):
        day_in_february = 29
    day_in_month = [31, day_in_february, 31,
                    30, 31, 30, 31, 31, 30, 31, 30, 31]
    seconds_in_month = [(i * 24 * 60 * 60) for i in day_in_month]
    month = 0
    while all > seconds_in_month[month]:
        all -= seconds_in_month[month]
        month += 1
    day = 1
    seconds_in_day = 24 * 60 * 60
    while all > seconds_in_day:
        all -= seconds_in_day
        day += 1
    seconds_in_hour = 60 * 60
    hour = 0
    while all > seconds_in_hour:
        all -= seconds_in_hour
        hour += 1
    minutes = 0
    seconds_in_minutes = 60
    while all > seconds_in_minutes:
        all -= seconds_in_minutes
        minutes += 1
    seconds = all
    month_name = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October',
                  'November', 'December']
    return '{} {} {} {}:{}:{}'.format(
        year, month_name[month], day, hour, minutes, seconds)


if __name__ == "__main__":
    time_stampt = "1526373175"
    print(timestamp_to_date1(time_stampt))
    print(timestamp_to_date2(time_stampt))
