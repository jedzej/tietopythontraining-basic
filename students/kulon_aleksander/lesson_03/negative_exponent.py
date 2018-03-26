def power(a, n):
    result = 1
    if n >= 0:
        for i in range(1, n + 1):
            result = result * a
        return result
    else:
        for i in range(n, 0):
            result = result / a
        return result


a = float(input())
n = int(input())

print(power(a, n))
