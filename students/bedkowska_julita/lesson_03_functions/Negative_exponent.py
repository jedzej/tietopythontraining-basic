base = float(input('Give the base: '))
expon = int(input('Give the exponent: '))


def pos_exp(a, n):
    result = 1
    for x in range(n):
        result *= a
    return result


def neg_exp(a, n):
    result = 1
    stop = n * -1
    for x in range(stop):
        result *= (1 / a)
    return result


if expon >= 0:
    exponent = pos_exp(base, expon)
else:
    exponent = neg_exp(base, expon)

print('{} {}'.format('Result:', exponent))
