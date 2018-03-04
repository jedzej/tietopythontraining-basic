# Problem «Car route» (Easy)
# Statement
# A car can cover distance of N kilometers per day.
# How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.
from math import ceil

print('Please input km/day:')
speed = int(input())
print('Please input length:')
length = int(input())

print('Distance can be travelled in: ' + str(ceil(length / speed)) + ' days')
