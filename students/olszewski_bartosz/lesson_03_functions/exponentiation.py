def exponentiation(a, n):
    result = 1
    if n == 0:
        return 1
    else:
        return a * exponentiation(a, n - 1)
        result *= a
    print(result)
print(exponentiation(float(input()), int(input())))
