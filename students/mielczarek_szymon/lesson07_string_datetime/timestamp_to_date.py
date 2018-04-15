from datetime import datetime
import time


def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')


if __name__ == '__main__':
    curr_timestamp = time.mktime(datetime.now().timetuple())
    print(timestamp_to_date(curr_timestamp))
