"""
Given a positive real number a and a non-negative integer n.
Calculate a ^ n without using loops, ** operator or the built in
function math.pow(). Instead, use recursion and the
relation an=a⋅an−1. Print the result.

Form the function power(a, n).
"""


def power(a, n):
    if n == 0:
        return 1
    elif a == 0:
        return 0
    else:
        if n == 1:
            return a
        else:
            return a * power(a, n - 1)


print("Please give numbers a ^ n:")
print("Please input a:")
a = float(input())
print("Please input n:")
n = int(input())

result = power(a, n)
print("Multiplication result = " + str(result))
