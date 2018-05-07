from datetime import datetime, timedelta

print("Enter the distance of the future date:")
number_of_years = int(input("Number of years="))
number_of_days = int(input("Number of days="))
number_of_hours = int(input("Number of hours="))
number_of_minutes = int(input("Number of minutes="))

current_date = datetime.now()
print('Current date = {:%Y-%m-%d %H:%M}'.format(datetime(current_date.year, current_date.month,
                                                         current_date.day, current_date.hour, current_date.minute)))

calculated_date = datetime(current_date.year + number_of_years, current_date.month, current_date.day,
                           current_date.hour, current_date.minute)

calculated_date = calculated_date + \
                  timedelta(days=number_of_days, hours=number_of_hours, minutes=number_of_minutes)

print('Future date  = {:%Y-%m-%d %H:%M}'.format(datetime(calculated_date.year, calculated_date.month,
                                                         calculated_date.day, calculated_date.hour,
                                                         calculated_date.minute)))
