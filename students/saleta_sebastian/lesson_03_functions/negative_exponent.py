def power(a, n):
    result = 1

    if (n > 0):
        result = a**n
    elif (n < 0):
        result = 1 / (a**abs(n))
    print(result)


a = float(input())
n = float(input())
power(a, n)
