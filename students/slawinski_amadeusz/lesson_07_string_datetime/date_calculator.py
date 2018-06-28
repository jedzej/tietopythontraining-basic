#!/urs/bin/env python3

import datetime

now = datetime.datetime.now()

now_unixtime = int(now.strftime("%s"))

print("Dodaj lat:")
years = int(input())
print("Dodaj dni:")
days = int(input())

print("Dodaj godzin:")
hours = int(input())
print("Dodaj minut:")
minutes = int(input())

addtime = minutes * 60 + \
    hours * 60 * 60 + \
    days * 24 * 60 * 60 + \
    years * 365 * 24 * 60 * 60 + \
    int(years / 4)

new_unixtime = now_unixtime + addtime

new_time = datetime.datetime.fromtimestamp(new_unixtime)

print(new_time.strftime("%H:%M %d.%m.%Y"))
