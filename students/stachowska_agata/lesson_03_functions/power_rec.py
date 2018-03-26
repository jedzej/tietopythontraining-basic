def power(a, n):
    result = 1
    while True:
        if n == 0:
            break
        result *= a
        n -= 1
    return result


a = float(input())
n = int(input())
print(power(a, n))
