import time
import calendar


def data_calculator(years=0, months=0, days=0, hours=0, minutes=0):
    current_minute = time.strftime("%M")
    full_minutes = int(current_minute) + minutes
    new_minute = int(full_minutes % 60)

    current_hour = time.strftime("%H")
    full_hours = int(current_hour) + hours + int(full_minutes / 60)
    new_hour = int(full_hours % 24)

    current_day = time.strftime("%d")
    full_days = int(current_day) + days + int(full_hours / 24)
    days_in_month = calendar.monthrange(int(time.strftime("%Y")),
                                        int(time.strftime("%m")))[1]
    new_day = int(full_days % days_in_month)

    current_month = time.strftime("%m")
    full_months = int(current_month) + months + int(full_days / days_in_month)
    new_month = int(full_months % 12)

    current_year = time.strftime("%Y")
    full_years = int(current_year) + years + int(full_months / 12)
    new_year = int(full_years)

    print(str(new_year) + '/' + str(new_month) + '/' + str(new_day) + ' ' +
          str(new_hour) + ':' + str(new_minute))


data_calculator(2, 45, 4, 60)
