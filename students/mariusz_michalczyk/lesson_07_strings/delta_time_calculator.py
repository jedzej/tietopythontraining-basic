from datetime import *


def get_user_input():
    print("Enter future date: ")
    entered_y = int(input("Enter year: "))
    entered_m = int(input("Enter month: "))
    entered_d = int(input("Enter day: "))
    return date(entered_y, entered_m, entered_d)


def current_date():
    return date(datetime.now().year,
                datetime.now().month,
                datetime.now().day)


if __name__ == '__main__':
    custom_date = get_user_input()
    print("Difference between your date and current date is: ")
    print(str((custom_date - current_date()).days) + " days")
