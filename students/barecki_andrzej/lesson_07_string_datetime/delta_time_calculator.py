import datetime


def main():
    now = datetime.datetime.now()
    print("Current date and time: {0:04}-{1:02}-{2:02} {3:02}:{4:02}:{5:02}"
          .format(now.year, now.month, now.day,
                  now.hour, now.minute, now.second))

    """"Set delta time"""
    year = int(input())
    month = int(input())
    day = int(input())

    """"Calculate difference between feature and current date"""
    delta_date = datetime.datetime(year=year, month=month, day=day) - now
    print("Total number of days to the feature date:{0}"
          .format(delta_date.days))


if __name__ == '__main__':
    main()
