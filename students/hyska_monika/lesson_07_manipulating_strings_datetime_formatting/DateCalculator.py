# Date calculator - function adds custom number of years,
# days and hours and minutes to current date
# and displays the result in human readable format.
import datetime


def add_to_date(date, years, months, days, hours, minutes):
    new_date = date + datetime.timedelta(days=days,
                                         hours=hours,
                                         minutes=minutes)
    years += (months + new_date.month) // 12
    months = (months + new_date.month) % 12
    new_date2 = new_date.replace(new_date.year + years, months)
    print('Changed date: ', new_date2.strftime("%Y-%m-%d %H:%M"))
    return new_date2


now = datetime.datetime.now()
print('Actual date and time: ', now.strftime("%Y-%m-%d %H:%M"))
add_to_date(now, 2, 4, 3, 5, 30)
add_to_date(now, 5, 15, 35, 28, 58)

test_date = datetime.datetime(1999, 11, 25, 23, 58)
print('\nCheck for date and time: ', test_date.strftime("%Y-%m-%d %H:%M"))
add_to_date(test_date, 5, 14, 35, 25, 58)
add_to_date(test_date, 2, 4, 3, 5, 30)
add_to_date(test_date, 5, 15, 35, 25, 58)
add_to_date(test_date, 5, 3, 7, 3, 4)
add_to_date(test_date, 5, 389, 455, 15897, 65)
