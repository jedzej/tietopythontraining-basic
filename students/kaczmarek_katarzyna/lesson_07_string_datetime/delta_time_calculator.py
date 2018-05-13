from datetime import datetime


def delta_time_calculator(date_to_compare):
    current_date = datetime.now()
    return str((date_to_compare - current_date).days)


def main():
    date_to_compare = datetime.strptime(
        input("Type a date (format: DD-MM-YYYY, ex. 05-06-2025): "),
        "%d-%m-%Y")
    print("Time difference: "
          + delta_time_calculator(date_to_compare) + " days")


if __name__ == '__main__':
    main()
