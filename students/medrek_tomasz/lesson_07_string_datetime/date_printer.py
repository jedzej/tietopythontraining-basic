#!/usr/bin/env python3


from datetime import datetime


def date_printer(date_to_print):
    print('{:{dfmt} {tfmt}}'.format(
        date_to_print, dfmt='%Y-%m-%d', tfmt='%H:%M'))


def main():
    date_printer(datetime.now())


if __name__ == "__main__":
    main()
