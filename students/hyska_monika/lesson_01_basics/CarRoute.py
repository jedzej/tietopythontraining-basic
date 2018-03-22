#This program returns numbers of days to cover road by car

import math

N = int(input("How many kilometers car can cover per day?: "))
M = int(input("How many kilometers car need cover?: "))

days = math.ceil(M / N)

print("To cover full road car needed", days, "day/s.")
