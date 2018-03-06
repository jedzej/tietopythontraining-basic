from math import modf

number = float(input("Enter number: "))

fract, real = modf(number)
print (round(fract, 6))