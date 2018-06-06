from datetime import datetime, timedelta

year = int(input('Years: '))
day = int(input('Days: '))
hour = int(input('Hours: '))
minute = int(input('Minutes: '))

current_date = datetime.now() + timedelta(weeks=year * 52, days=day,
                                          hours=hour, minutes=minute)
print('The new date is: ' + current_date.strftime("%d-%m-%Y %H:%M:%S"))
