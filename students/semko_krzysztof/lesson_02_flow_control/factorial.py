"""
In mathematics, the factorial of an integer n,
denoted by n! is the following product:
n!=1×2×…×n

For the given integer n
calculate the value n!. Don't use math module in this exercise.
"""

print("Please input an integer value:")
n = int(input())
result = 1
for i in range(n):
    result *= (i + 1)
print("Factorial result: " + str(n) + "! = " + str(result))
