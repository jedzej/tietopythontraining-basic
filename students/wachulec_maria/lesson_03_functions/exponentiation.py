def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


a = float(input("a: "))
n = int(input("n: "))
result = power(a, n)
print(result)
