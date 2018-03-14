"""
description: 1! + 2! + ... + n!
    This problem has a solution with only one loop, so try to discover it.
    And don't use the math library :)
"""

print("For given n returns 1! + 2! + ... + n!.")

n = int(input("n = "))

factorial = 1
sum = 0

if n > 0:
    for k in range(1, n+1):
        factorial *= k
        sum += factorial

print(sum)
