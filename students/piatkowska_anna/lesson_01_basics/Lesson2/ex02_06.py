#Statement
#A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.
print("Please enter how many kilometers per day your car can cover:")
a = int(input())
print("Please enter length of a route:")
b = int(input())
import math
print("It takes " + str(math.ceil(b/a)) + " day(s) to cover a route.")