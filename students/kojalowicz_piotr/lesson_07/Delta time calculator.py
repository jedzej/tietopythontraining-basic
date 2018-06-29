from datetime import datetime


def delta_time_calculator(date):
    date_format = "%d/%m/%Y"
    today = datetime.now()
    future_date = datetime.strptime(date, date_format)
    return (future_date - today).days


# '9/26/2018'
print(delta_time_calculator('23/9/2018'))
print(datetime.now().timetuple().tm_yday)
