def power(a, n):
    counter = 0
    result = 1
    sign = 1
    if n == 0:
        return 1
    if n < 0:
        sign = -1
        n = n * -1
    for counter in range(1, n+1):
        if sign > 0:
            result = result * a
        else:
            result = result / a
    return result

a = float(input())
n = int(input())
r = power(a, n)
print(r)

