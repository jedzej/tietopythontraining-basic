#!/usr/bin/env python3


import time
from datetime import datetime
from date_printer import date_printer


def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp)


def main():
    date_printer(timestamp_to_date(time.time()))


if __name__ == "__main__":
    main()
