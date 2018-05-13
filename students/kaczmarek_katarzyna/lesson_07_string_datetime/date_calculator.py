from date_printer import date_printer
from datetime import datetime, timedelta


def date_calculator(current_date, years, days, hours, minutes):
    days += 365.25 * years
    new_date = \
        current_date + timedelta(days=days, hours=hours, minutes=minutes)

    return date_printer(new_date)


def main():
    years = int(input("Type years: "))
    days = int(input("Type days: "))
    hours = int(input("Type hours: "))
    minutes = int(input("Type minutes: "))

    current_date = datetime.now()

    print("Current date: " + date_printer(current_date))
    print("Modified date: " +
          date_calculator(current_date, years, days, hours, minutes))


if __name__ == '__main__':
    main()
