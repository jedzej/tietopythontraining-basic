import time
import datetime


def get_date_from_timestamp(timestamp):
    return datetime \
        .datetime \
        .fromtimestamp(timestamp) \
        .strftime('%Y-%m-%d %H:%M:%S')


def get_timestamp():
    return time.time()


def main():
    print(get_date_from_timestamp(get_timestamp()))


if __name__ == '__main__':
    main()