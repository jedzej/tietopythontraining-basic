from datetime import *


def add_to_current_date(y, d, h, m):
    now = datetime.now()
    return now + timedelta(days=(y * 365) + d, hours=h, minutes=m)


def get_user_input():
    print("Enter customized date: ")
    entered_y = int(input("Enter year which want to add : "))
    entered_d = int(input("Enter day which want to add: "))
    entered_h = int(input("Enter hour which want to add: "))
    entered_m = int(input("Enter minutes which want to add: "))
    return add_to_current_date(entered_y, entered_d, entered_h, entered_m)


if __name__ == '__main__':
    new = get_user_input()
    print("Customized date is {0} year {1} month and {2} day. Time is: {3}".
          format(new.year, new.month, new.day, new.strftime("%H:%M")))
