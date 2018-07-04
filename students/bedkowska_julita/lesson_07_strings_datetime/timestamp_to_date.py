import datetime


def date_from_timestamp(timestmp):
    print('Result: ')
    print('{:%Y-%m-%d}'.format(datetime.datetime.fromtimestamp(timestmp)))


timestamp = int(input('Input the timestamp format: '))
date_from_timestamp(timestamp)
