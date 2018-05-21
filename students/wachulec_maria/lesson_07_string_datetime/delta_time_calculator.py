from datetime import datetime, timedelta


def create_custom_date(year, day, hour, minute):
    shift_date = datetime.now() + timedelta(days=365.25 * year + day,
                                            hours=hour, minutes=minute)
    return shift_date


def calculate_days_difference(date):
    actual_date = datetime.now()
    return (date - actual_date).days


future_date = create_custom_date(1, 2, 8, 10)
print(calculate_days_difference(future_date))
