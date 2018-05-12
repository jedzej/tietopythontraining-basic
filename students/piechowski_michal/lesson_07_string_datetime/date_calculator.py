#!/usr/bin/env python3

import datetime


def main():
    current_date = datetime.datetime.now()
    years_shift, days_shift, hours_shift, minutes_shift = 17, 5, 21, 52
    days_shift += abs(years_shift * 365.25)

    future_date = current_date + datetime.timedelta(
        days=days_shift, hours=hours_shift, minutes=minutes_shift)

    print(future_date)


if __name__ == "__main__":
    main()
