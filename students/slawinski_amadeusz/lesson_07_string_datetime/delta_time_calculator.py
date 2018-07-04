#!/usr/bin/env python3

import datetime
import time


def delta_time(deltatime):
    now = datetime.datetime.now()
    now_unixtime = int(now.strftime("%s"))

    time_unixtime = int(deltatime.strftime("%s"))

    if now_unixtime >= time_unixtime:
        print("Podaj datę w przyszłości")
    else:
        print("Różnica czasu to: {} dni".format((deltatime - now).days))


if __name__ == "__main__":
    print("Podaj datę (HH:MM DD.MM.YYYY):")
    date = input()
    a = time.strptime(date, '%H:%M %d.%m.%Y')

    dt = datetime.datetime.fromtimestamp(time.mktime(a))

    delta_time(dt)
