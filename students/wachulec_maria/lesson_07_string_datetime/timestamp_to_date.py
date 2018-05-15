from datetime import datetime


def print_date_from_timestamp():
    timestamp = datetime.timestamp(datetime.now())
    return '{:%Y-%m-%d %H:%M:%S}'.format(datetime.fromtimestamp(timestamp))


print(print_date_from_timestamp())
