from datetime import datetime
from datetime import timedelta

future_days = timedelta(days=int(input("How many days into future: ")))
future_years = timedelta(days=(int(input("How many years into future: ")))*365)
future_minutes = timedelta(minutes=(int(input("How many minutes into future: ")))*365)
future_hours= timedelta(hours=(int(input("How many hours into future: "))))

print(datetime.now()+future_days+future_years+future_minutes+future_hours)


