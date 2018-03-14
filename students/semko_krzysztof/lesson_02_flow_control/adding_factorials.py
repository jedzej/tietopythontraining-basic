"""
Given an integer n, print the sum 1!+2!+3!+...+n!.

This problem has a solution with only one loop,
so try to discover it. And don't use the math library :)
"""

print("Please input an integer value:")
n = int(input())

factorial = 1
result = 0

for i in range(1, n + 1):
    factorial *= i
    result += factorial

print("Sum of factorials: " + str(result))
