# https://snakify.org/lessons/functions/problems/power_rec/
# piotrsta


def power(a, n):
    if float(n) == 0:
        return 1
    else:
        return float(a) * power(float(a), float(n) - 1)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


a = input()
n = input()

if is_float(a) and is_float(n):
    print(power(a, n))
else:
    print('Wrong input values.')
