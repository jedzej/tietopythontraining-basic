from datetime import datetime, timedelta


years = 2
days = 2
hours = 2
minutes = 2

current_datetime = datetime.now()
days += years * 365
print(current_datetime + timedelta(days=days, hours=hours, minutes=minutes))
