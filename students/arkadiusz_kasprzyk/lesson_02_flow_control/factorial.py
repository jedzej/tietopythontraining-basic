"""
description: n!
"""

print("For given n returns n! (factorial).")

n = int(input("n = "))
factorial = 1

if n > 0:
    for k in range(1, n+1):
        factorial *= k

print(factorial)
