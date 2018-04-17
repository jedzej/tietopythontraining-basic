def exponentiation(a, n):
    result = 1
    if n < 0:
        print("Error n cannot be less than 0")
        return ValueError
    elif n == 0:
        return 1
    else:
        return a * exponentiation(a, n - 1)
        result *= a
    print(result)


print(exponentiation(float(input()), int(input())))
