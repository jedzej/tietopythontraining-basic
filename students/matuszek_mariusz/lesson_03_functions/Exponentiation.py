def power(x, y):
    res = x

    for i in range(y-1):
        res = res * x

    return res


while True:
    a = float(input('a = '))

    if a >= 0:
        break
    else:
        print("'a' should be positive real number !!")
        continue

while True:
    n = int(input('n = '))

    if n >= 0:
        break
    else:
        print("'n' should be non-negative integer !!")
        continue

print(power(a, n))
