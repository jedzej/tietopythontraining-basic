def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


base = float(input("Base number: "))
powering = int(input("Power number: "))
print(power(base, powering))
