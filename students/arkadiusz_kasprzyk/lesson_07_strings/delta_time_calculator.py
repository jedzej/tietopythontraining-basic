#! python
# delta_time_calculator.py

import datetime as dt


def time_diff(year, month, day):
    date = dt.date(year, month, day)
    return date - dt.date.today()


if __name__ == "__main__":
    print("Give future date:")
    tdiff = time_diff(year=int(input("year: ")),
                      month=int(input("month: ")),
                      day=int(input("day: ")))
    print("There is difference of {} days.".format(tdiff.days))
