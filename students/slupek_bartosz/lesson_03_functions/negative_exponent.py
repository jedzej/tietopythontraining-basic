def power(a, n):
    result = 1
    if n > 0:
        for i in range(n):
            result *= a
    elif n < 0:
        a = 1 / a
        for i in range(abs(n)):
            result *= a
    return result


print(power(float(input()), int(input())))
