from math import modf
number = float(input("Enter number: "))

fract, real = modf(number)

print (str(fract)[2])


