# Given an integer n, print the sum 1!+2!+3!+...+n!.
# This problem has a solution with only one loop, so try to discover it.
# And don't use the math library :)

n = int(input())

factorial = 1
result = 0
for x in range(1, n + 1):
    factorial *= x
    result += factorial

print(result)
