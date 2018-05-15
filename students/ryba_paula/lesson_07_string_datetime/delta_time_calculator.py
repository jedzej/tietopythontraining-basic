from datetime import datetime


def delta_time_calculator(y, m, d):
    current_date = datetime.now()
    future_date = datetime(y, m, d)

    return str((future_date - current_date).days)


def main():
    y = int(input("Input year: "))
    m = int(input("Input month: "))
    d = int(input("Input day: "))

    print("Time difference: " + delta_time_calculator(y, m, d) + " days")


if __name__ == '__main__':
    main()
