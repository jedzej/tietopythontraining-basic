"""
Given a positive real number a and integer n.
Compute a^n. Write a function power(a, n) to calculate
the results using the function and print the result of the expression

Don't use the same function from the standard library.
"""

print("Operation a ^ n :")
print("Please input the 'a' value:")
a = float(input())
print("Please input the 'n' value:")
n = int(input())

result = a
for i in range(1, abs(n)):
    result *= a

if n < 0:
    result = 1 / result

print("Result of a ^ n = " + str(result))
