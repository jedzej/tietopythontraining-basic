def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


if __name__ == '__main__':
    var1 = float(input())
    var2 = int(input())
    print (power(var1, var2))
