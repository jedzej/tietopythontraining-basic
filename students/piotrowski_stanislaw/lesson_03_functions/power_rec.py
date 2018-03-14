# https://snakify.org/lessons/functions/problems/power_rec/
# piotrsta

a = float(input())
n = float(input())

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(a, n))
