import datetime

now = datetime.datetime.now()

print("Current time is: \n"
      "Day: %d \n"
      "Month: %d\n"
      "Year: %d\n"
      "Hour: %d\n"
      "Minut: %d\n"% (now.day, now.month, now.year, now.hour, now.minute))

