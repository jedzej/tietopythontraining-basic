#! python
# date_calculator.py

import datetime as dt


def time_from_now(years=0, days=0, hours=0, minutes=0):
    """
    Examples
    --------
    time_from_now()
    time_from_now(2, 33, 12, 3)
    """
    date0 = dt.datetime.now()
    date1 = date0.replace(date0.year + years) + \
        dt.timedelta(days=days, hours=hours, minutes=minutes)
    return date1


if __name__ == "__main__":
    print("Give years, days, hours, minutes from now:")
    dateout = time_from_now(years=int(input("years: ")),
                            days=int(input("days: ")),
                            hours=int(input("hours: ")),
                            minutes=int(input("minutes: ")))
    print("{:%Y-%m-%d %H:%M}".format(dateout))
