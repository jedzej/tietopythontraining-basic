import datetime


def delta_time_calculator(date_in_the_future):
    current_date = datetime.date.today()
    diff = date_in_the_future - current_date
    result = diff.days
    print(result)


def main():
    print("Today:")
    print(datetime.date.today())
    print("Enter year in future:")
    year = int(input())
    print("Enter month in future:")
    month = int(input())
    print("Enter day in future:")
    day = int(input())
    date_in_the_future = datetime.date(year, month, day)
    print("Difference in days between current date and date in the future:")
    delta_time_calculator(date_in_the_future)


if __name__ == "__main__":
    main()
