base = float(input())
expon = int(input())


def exponentiation(a, n):
    if n == 0:
        return 1
    else:
        return a * exponentiation(a, n - 1)


print('{} {}'.format('Result:', exponentiation(base, expon)))
