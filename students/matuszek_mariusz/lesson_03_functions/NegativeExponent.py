import math


def power(x, y):
    return math.pow(x, y)


while True:
    a = float(input('a = '))

    if a >= 0:
        break
    else:
        print("'a' should be positive !!")
        continue

while True:
    n = input('n = ')

    try:
        n = int(n)
        break

    except ValueError:
        print('Enter an integer !!')
        continue

print(power(a, n))
