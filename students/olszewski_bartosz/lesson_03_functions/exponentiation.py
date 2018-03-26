def exponentiation(a, n):
    result = 1
    if n == 0:
        return 1
    result *= a
    return a * exponentiation(a, n - 1)
    print(result)


print(exponentiation(float(input()), int(input())))

