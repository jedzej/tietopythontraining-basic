from math import ceil 

# Read an integer:
a = float(input())
b = float(input())
n = int(input())

total_cost = ((a + (b / 100)) * n)

print(int(total_cost), round((total_cost - int(total_cost)) * 100))
