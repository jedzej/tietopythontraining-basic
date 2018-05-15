from date_printer import date_printer
from datetime import datetime, timedelta

current_date = datetime.now()


def date_calculator(y, d, h, m):
    d += 365.25 * y
    new_date = current_date + timedelta(days=d, hours=h, minutes=m)

    return date_printer(new_date)


def main():
    y = int(input("Input years: "))
    d = int(input("Input days: "))
    h = int(input("Input hours: "))
    m = int(input("Input minutes: "))

    print("Current time is: " + date_printer(current_date))
    print("New time is: " + date_calculator(y, d, h, m))


if __name__ == '__main__':
    main()
