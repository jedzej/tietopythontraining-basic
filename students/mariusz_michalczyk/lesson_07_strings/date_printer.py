from datetime import datetime


if __name__ == '__main__':
    now = datetime.now()
    print("Today is {0} year {1} month and {2} day. Time is: {3}".
          format(now.year, now.month, now.day, now.strftime("%H:%M")))
