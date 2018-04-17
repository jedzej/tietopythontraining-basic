def power(a, n):
    if n >= 1:
        return a * power(a, n - 1)
    elif n == 0:
        return 1


a = float(input("Enter a number: "))
n = int(input("Enter the exponent: "))
print(power(a, n))
