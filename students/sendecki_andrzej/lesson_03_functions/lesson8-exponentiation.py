#Given a positive real number a and a non-negative integer n. Calculate a^n without using loops, ** operator or the built in function math.pow(). Instead, use recursion and the relation a^n=a⋅a^n−1. Print the result.
#
#Form the function power(a, n).

import sys

def power(a, n):
    if (n == 0):
        return 1
    else:
        return (a * power(a, n-1))

print("Enter real:")
a = float(input())
if (a <= 0):
    print("Error: non-positive number entered.")
    sys.exit()

print("Enter integer:")
n = int(input())
if (n < 0):
    print("Error: negative number entered.")
    sys.exit()

print(power(a, n))
