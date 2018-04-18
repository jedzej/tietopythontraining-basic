from datetime import datetime

year = int(input('Year: '))
months = int(input('Month: '))
days = int(input('Day: '))
print("Difference in days: " + str((datetime(year, months, days) - datetime.now()).days))
