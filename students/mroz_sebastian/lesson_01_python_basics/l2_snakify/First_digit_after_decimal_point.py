from math import floor
a = float(input())

first_decimil_digit = floor(a*10) % 10
print(first_decimil_digit)
