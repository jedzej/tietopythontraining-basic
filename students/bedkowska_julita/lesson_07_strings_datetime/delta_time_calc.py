import datetime

future_date = input('Give the date (format RRRR-MM-DD): ')
year = int(future_date[0:4])
month = int(future_date[5:7])
day = int(future_date[8:])

current_date = datetime.datetime.now()
delta = datetime.datetime(year, month, day)
difference = delta - current_date
print('Difference: ' + str(difference)[:8])
