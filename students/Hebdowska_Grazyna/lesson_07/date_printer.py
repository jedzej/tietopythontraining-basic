import time
from datetime import datetime


def date_printer():
    dt = time.localtime()
    year = dt[0]
    month = dt[1]
    day = dt[2]
    print('{:%Y-%m-%d}'.format(datetime(year, month, day)))


date_printer()
