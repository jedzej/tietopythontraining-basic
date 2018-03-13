def power(a, n):
    result = 1.0
    if n > 0:
        for i in range(n):
            result *= a
    elif n == 0:
        result = 1
    else:
        for i in range(abs(n)):
            result *= 1 / a
    return result


a = float(input("Enter a number: "))
n = int(input("Enter the exponent: "))

print(power(a, n))
