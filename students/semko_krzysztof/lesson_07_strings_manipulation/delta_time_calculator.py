"""
Delta time calculator - write a script that calculates
time difference in days between current date and
custom date in the future.
"""
from datetime import date
from datetime import timedelta


def main():
    print("Please input future year:")
    year = int(input())
    print("Please input future month:")
    month = int(input())
    print("Please input future day:")
    day = int(input())

    current = date.today()
    future = date(year, month, day)
    print((future - current).days)


if __name__ == '__main__':
    main()
