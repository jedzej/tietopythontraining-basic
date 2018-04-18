from datetime import datetime, timedelta

year = int(input('Years to add: '))
day = int(input('Days to add: '))
hour = int(input('Hours to add: '))
minute = int(input('Minutes to add: '))

current_date = datetime.now() + timedelta(weeks=year * 52, days=day,
                                          hours=hour, minutes=minute)
print('Date after change: ' + current_date.strftime("%d-%m-%Y %H:%M:%S"))
