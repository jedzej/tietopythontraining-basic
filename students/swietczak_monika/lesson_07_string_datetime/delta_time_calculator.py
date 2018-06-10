from datetime import datetime

today = datetime.now()
y = int(input("Input year: "))
m = int(input("Input month: "))
d = int(input("Input day: "))

custom_date = datetime(year=y, month=m, day=d)

print("The difference is " + str(abs((today - custom_date).days)) + " days")
