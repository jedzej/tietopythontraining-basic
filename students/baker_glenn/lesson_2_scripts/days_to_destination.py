# script to calculate the amount of days to arrive at a destination given km's per day and total distance
import math

print("enter a the amount of km's per day")
km_per_day = int(input())
print("enter a the total distance")
total_distance = int(input())
print("it will take " + str(math.ceil(total_distance / km_per_day)) + " days to arrive at the destination")
