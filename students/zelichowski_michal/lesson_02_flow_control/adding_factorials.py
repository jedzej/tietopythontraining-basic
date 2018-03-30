"""Given an integer n, print the sum 1!+2!+3!+...+n!.

This problem has a solution with only one loop, so try to discover it.
And don't use the math library :) """

# Read an integer:
n = int(input())
factorial = 1
sum = 0

# Print a value:
for x in range(1, n + 1):
    factorial = factorial * x
    sum += factorial
print(sum)
