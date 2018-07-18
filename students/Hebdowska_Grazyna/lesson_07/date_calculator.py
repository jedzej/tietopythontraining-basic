import time
from datetime import datetime


def custom_number_data():

    cnd = float(input("Give  number of years: ")) * 365 * 24 * 3600
    cnd = cnd + float(input("Give  number of month: ")) * 30 * 24 * 3600
    cnd = cnd + float(input("Give  number of days: ")) * 24 * 3600
    cnd = cnd + float(input("Give  number of houers: ")) * 3600
    cnd = cnd + float(input("Give  number of minutes: ")) * 60

    return cnd


def conwert_time(t):
    new_t = time.time() + t
    dt = time.localtime(new_t)
    year = dt[0]
    month = dt[1]
    day = dt[2]
    houer = dt[3]
    min = dt[5]
    print('{:%Y-%m-%d  %H:%M}'.format(datetime(year, month, day, houer, min)))


t = custom_number_data()
conwert_time(t)
