from datetime import datetime, timedelta


def calculate_date(years, days, hours, minutes):
    date = datetime.now()
    shift_date = date + timedelta(days=365.25 * years + days, hours=hours,
                                  minutes=minutes)
    return '{:%Y-%m-%d %H:%M:%S}'.format(shift_date)


print(calculate_date(1, 2, 3, 1))
