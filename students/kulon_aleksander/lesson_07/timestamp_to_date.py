from datetime import datetime
import time


def timestamp_to_date(timestamp):
    print(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))


def main():
    curr_timestamp = time.mktime(datetime.now().timetuple())
    timestamp_to_date(curr_timestamp)


if __name__ == '__main__':
    main()
