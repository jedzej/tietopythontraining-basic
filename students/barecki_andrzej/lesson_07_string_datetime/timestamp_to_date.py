import datetime
import time


def main():
    """"Generate timestamp"""
    timestamp = time.time()
    print("Current timestamp: {0}".format(timestamp))

    """"Convert timestamp to date and time"""
    now = datetime.datetime.fromtimestamp(timestamp)
    print("Current date and time: {0:04}-{1:02}-{2:02} {3:02}:{4:02}:{5:02}"
          .format(now.year, now.month, now.day,
                  now.hour, now.minute, now.second))


if __name__ == '__main__':
    main()
