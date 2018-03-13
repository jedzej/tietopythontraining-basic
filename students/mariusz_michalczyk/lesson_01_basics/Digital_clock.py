from math import *
passed_minutes = int(input("Enter minutes: "))
day_minutes = passed_minutes % 1440
print (str(day_minutes // 60) + " " +  str(day_minutes % 60))




