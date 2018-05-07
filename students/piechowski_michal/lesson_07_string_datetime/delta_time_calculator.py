#!/usr/bin/env python3

import datetime


def main():
    current_date = datetime.datetime.now()
    future_date = datetime.datetime(year=2130, month=7, day=19)

    print((future_date - current_date).days)


if __name__ == "__main__":
    main()
