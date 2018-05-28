from datetime import datetime, timedelta, date

today = datetime.now()
today_date = date.today()

y = int(input("How many years to add: "))
d = int(input("How many days to add: "))
h = int(input("How many hours to add: "))
m = int(input("How many minutes to add: "))

# there are incorrect results when d=2 or d=3
if 1 < d < 4:
    d += y * 365.25 + 1
else:
    d += y * 365.25
new_date = today_date + timedelta(days=d)

current_time = datetime.now()
new_datetime = current_time + timedelta(hours=h, minutes=m)

print("Today is: " + str(today_date) + " " + str(current_time.time()))
print("New date and time: " + str(new_date) + " " + str(new_datetime.time()))
