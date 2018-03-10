from math import ceil

range_per_day = int(input())
distance = int(input())

days = ceil(distance / range_per_day)

print(days)
