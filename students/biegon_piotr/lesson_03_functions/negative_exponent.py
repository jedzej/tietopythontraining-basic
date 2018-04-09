print("Negative exponent\n")


def power(a, n):
    return a ** n


a = float(input("Enter a power base: "))
n = int(input("Enter an exponent exponent: "))

print("\nThe result is: {:f}".format(power(a, n)))
