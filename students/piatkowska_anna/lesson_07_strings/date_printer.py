'''
Date printer - write a script that displays
current date in human-readable format
'''
from datetime import datetime


def current_date():
    now = datetime.now()
    return '{:%A %Y %B %d %H:%M (week number:%U)}'.format(now)


if __name__ == "__main__":
    print("Current date:")
    print(current_date())
