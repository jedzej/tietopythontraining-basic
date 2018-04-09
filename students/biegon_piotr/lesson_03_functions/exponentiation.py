print("Exponentiation\n")


def power(a, n):
    if n == 0:
        return 1
    if n >= 1:
        return a * power(a, n-1)


a = float(input("Enter a power base: "))
n = int(input("Enter an exponent exponent: "))

print("\nThe result is: {:f}".format(power(a, n)))
