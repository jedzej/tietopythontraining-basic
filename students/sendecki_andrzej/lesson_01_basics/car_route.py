# lesson_01_basics
# Car route
#
# Statement
# A car can cover distance of N kilometers per day.
# How many days will it take to cover a route of length M kilometers?
# The program gets two numbers: N and M. 

import math

print("Enter the number of kilometers/day")
N = int(input())

print("Enter the route length")
M = int(input())

res = math.ceil(M / N)

print("It will take " + str(res) + " day(s).")

