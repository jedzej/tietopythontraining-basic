from datetime import datetime


def print_actual_date():
    return '{:%Y-%m-%d %H:%M}'.format(datetime.now())


print(print_actual_date())
