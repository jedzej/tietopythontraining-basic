from datetime import datetime, timedelta


if __name__ == '__main__':
    current_datetime = datetime.now()
    years, days, hours, minutes = 2, 3, 4, 5
    # Take a fixed number of days in a year
    days += years * 365
    print(current_datetime + timedelta(days=days, hours=hours, minutes=minutes))
