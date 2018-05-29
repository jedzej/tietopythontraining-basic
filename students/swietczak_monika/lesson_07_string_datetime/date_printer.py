from datetime import datetime

now = datetime.now()
# print(str(now))
print(now.strftime("Today is: %d.%m.%Y"))
print(now.strftime("Current time: %H:%M"))
