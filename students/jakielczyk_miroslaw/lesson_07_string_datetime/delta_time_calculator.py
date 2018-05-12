from datetime import datetime

print("Enter the future date:")
year = int(input("Year="))
month = int(input("Month="))
day = int(input("Day="))

current_time = datetime.now()
date_in_future = datetime(year, month, day)
date_difference = date_in_future - current_time

print("Difference between future and current date:", date_difference.days, "days")
