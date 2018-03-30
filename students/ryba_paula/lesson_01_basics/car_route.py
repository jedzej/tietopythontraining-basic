from math import ceil

km_per_day, route = int(input()), int(input())

print(ceil(route / km_per_day))