# The program print digits sum for integer.

a = int(input("Please put integer number: "))

s = sum(map(int, str(a)))

print("The sum of digits is:", s)
