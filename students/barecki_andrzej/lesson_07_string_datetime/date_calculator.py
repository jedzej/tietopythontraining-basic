import datetime


def main():
    now = datetime.datetime.now()
    print("Current date and time: {0:04}-{1:02}-{2:02} {3:02}:{4:02}:{5:02}"
          .format(now.year, now.month, now.day,
                  now.hour, now.minute, now.second))

    """"Set delta time"""
    years = int(input())
    days = int(input())
    hours = int(input())
    minutes = int(input())

    """"Calculate feature date and time"""
    feature = now + datetime.timedelta(days=years * 365 + days,
                                       hours=hours,
                                       minutes=minutes)
    print("Feature date and time: {0:04}-{1:02}-{2:02} {3:02}:{4:02}:{5:02}"
          .format(feature.year, feature.month, feature.day,
                  feature.hour, feature.minute, feature.second))


if __name__ == '__main__':
    main()
