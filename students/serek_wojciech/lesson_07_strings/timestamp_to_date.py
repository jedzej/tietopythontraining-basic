#!/usr/bin/env python3
"""Date printer exercise"""
import datetime
import time
from date_printer import date_printer


def timestamp_to_date(time_stamp):
    """Date printer function"""
    return date_printer(datetime.datetime.fromtimestamp(time_stamp))


def main():
    """Main function"""
    print(timestamp_to_date(time.time()))


if __name__ == '__main__':
    main()
