#!/usr/bin/env python3
"""Delta time calculator exercise"""
import datetime


def delta_time_calculator(year, month, day):
    """Calculates date difference in days"""
    return((datetime.datetime(year, month, day) -
            datetime.datetime.now()).days)


def main():
    """Main function"""
    year = int(input('Year: '))
    month = int(input('Month: '))
    day = int(input('Day: '))

    print("Time difference in days:" + str(delta_time_calculator(year, month,
                                                                 day)))


if __name__ == '__main__':
    main()
