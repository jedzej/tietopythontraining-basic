# https://snakify.org/lessons/functions/problems/negative_power/
# piotrsta


def power(a, n):
    result = a ** n
    return result


a = float(input())
n = float(input())

print(power(a, n))
