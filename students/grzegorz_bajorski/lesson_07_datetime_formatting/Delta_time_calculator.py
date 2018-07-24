from datetime import datetime


current_datetime = datetime.now()
future_datetime = datetime(year=2143, month=12, day=3)
print((future_datetime - current_datetime).days)
