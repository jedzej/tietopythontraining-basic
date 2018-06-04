from datetime import datetime

current_date = datetime.now()

d = int(input("Day: "))
m = int(input("Month: "))
y = int(input("Year: "))

custom_date = datetime(day=d, month=m, year=y)

print("The difference is " + str(abs((current_date - custom_date).days)) +
      " days")
