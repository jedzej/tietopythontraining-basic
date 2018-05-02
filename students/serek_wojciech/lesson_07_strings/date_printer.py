#!/usr/bin/env python3
"""Date printer exercise"""
import datetime


def date_printer(date_time):
    """Date printer function"""
    return '{:%Y-%m-%d %H:%M:%S}'.format(date_time)


def main():
    """Main function"""
    print(date_printer(datetime.datetime.now()))


if __name__ == '__main__':
    main()
