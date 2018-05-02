def power(base, exponent):
    result = 1.0
    if exponent > 0:
        for i in range(exponent):
            result *= base
    elif exponent == 0:
        result = 1
    else:
        for i in range(abs(exponent)):
            result *= 1 / base
    return result


a = float(input("Enter a number: "))
n = int(input("Enter the exponent: "))

print(power(a, n))
