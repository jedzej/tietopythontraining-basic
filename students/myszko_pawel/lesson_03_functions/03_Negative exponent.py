# Given a positive real number a and integer n.
# Compute an. Write a function power(a, n) to calculate the results using the function and print the result of the expression.
# Don't use the same function from the standard library.

# Read an integer:
a = float(input())
n = int(input())
# Print a value:
def power(a, n):
    result = 1
    if n > 0:
        for i in range(1, n+1):
            result = a*result
        return result
    elif n < 0:
        result = a**n
        return result
    elif n == 0:
        return 1

print(power(a, n))