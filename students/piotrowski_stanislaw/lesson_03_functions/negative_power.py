# https://snakify.org/lessons/functions/problems/negative_power/
# piotrsta


def power(a, n):
    result = float(a) ** int(n)
    return result


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


a = input('Enter float value: ')
n = input('Enter integer value: ')

if is_float(a) and is_int(n):
    print(power(a, n))
else:
    print('Wrong input values.')
