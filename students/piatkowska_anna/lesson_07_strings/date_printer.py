'''
Date printer - write a script that displays
current date in human-readable format
'''
from datetime import datetime


def current_date():
    now = datetime.now()
    months = {1: "January", 2: "February", 3: "Mars", 4: "April", 5: "May",
              6: "June", 7: "July", 8: "August", 9: "September",
              10: "October", 11: "November", 12: "December"}
    return '{:%A %Y %B %d %H:%M (week number:%U)}'.format(now)


if __name__ == "__main__":
    print("Current date:")
    print(current_date())
