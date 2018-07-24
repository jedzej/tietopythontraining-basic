from datetime import date
import datetime

now = datetime.datetime.now()

future_date = date(int(input("Type year in the future: ")), int(input("Type month in the future: ")), int(input("Type day in the future: ")))
now_date = date(now.year, now.month, now.day)
delta = future_date - now_date
print(delta.days)