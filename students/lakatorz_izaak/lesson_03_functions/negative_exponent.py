# Compute an. Write a function power(a, n) to calculate the results using
# the function and print the result of the expression.


def power(a, n):
    if n < 0:
        a = 1 / a
        n *= -1

    result = 1

    while n > 0:
        result *= a
        n -= 1
    return result


print("Enter base (a):")
base = float(input())

print("Enter exponent (n):")
exponent = int(input())

print(power(base, exponent))
