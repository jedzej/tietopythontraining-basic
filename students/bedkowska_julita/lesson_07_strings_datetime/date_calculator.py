import datetime

years = int(input('Input the number od years: '))
days = int(input('Input the number of days: '))
hours = int(input('Input the number of hours: '))
minutes = int(input('Input the number of minutes: '))

current_date = datetime.datetime.now()
output_date = current_date.replace(year=current_date.year + years) \
              + datetime.timedelta(days=days, hours=hours, minutes=minutes)
print('Result: ')
print("{:%Y-%m-%d %H:%M}".format(output_date))
