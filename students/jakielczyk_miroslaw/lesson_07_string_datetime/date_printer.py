from datetime import datetime

current_date = datetime.now()
print('{:%Y-%m-%d %H:%M:%S}'.format(datetime(current_date.year, current_date.month,
                                             current_date.day, current_date.hour,
                                             current_date.minute, current_date.second)))
