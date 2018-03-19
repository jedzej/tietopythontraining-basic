# https://snakify.org/lessons/functions/problems/power_rec/
# piotrsta


def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a = float(input())
n = float(input())

print(power(a, n))
