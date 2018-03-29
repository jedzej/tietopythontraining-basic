def power(a, n):
    result = 1

    if n > 0:
        result = a**n
    elif n < 0:
        result = 1 / (a**abs(n))
    print(result)


if __name__ == '__main__':
    var1 = float(input())
    var2 = float(input())
    power(var1, var2)
