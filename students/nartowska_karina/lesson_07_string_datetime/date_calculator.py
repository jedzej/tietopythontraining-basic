import datetime


def date_calculator(add_years, add_days, add_hours, add_minutes):
    current_date = datetime.datetime.now()
    add_days += add_years * 365.25
    date_in_the_future = current_date + datetime.timedelta(
        days=add_days, hours=add_hours, minutes=add_minutes)

    print(date_in_the_future)


def main():
    print("How many years add to current date?")
    add_years = int(input())
    print("How many days add to current date?")
    add_days = int(input())
    print("How many hours add to current date?")
    add_hours = int(input())
    print("How many minutes add to current date?")
    add_minutes = int(input())

    print("Result:")
    date_calculator(add_years, add_days, add_hours, add_minutes)


if __name__ == "__main__":
    main()

