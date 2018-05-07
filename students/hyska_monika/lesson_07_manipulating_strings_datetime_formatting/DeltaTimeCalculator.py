# Delta time calculator - script that calculates time difference
# in days between current date and custom date in the future.
import datetime


def different_in_days(date, date2):
    delta = date2 - date
    print('Different in days: ', delta.days)
    return delta.days


now = datetime.datetime.now()
feature_date = datetime.datetime(2020, 10, 6, 13, 22)
print('Actual date and time: ', now.strftime("%Y-%m-%d %H:%M"))
print('Feature date and time: ', feature_date.strftime("%Y-%m-%d %H:%M"))

different_in_days(now, feature_date)
