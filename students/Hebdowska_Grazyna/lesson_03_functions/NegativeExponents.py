def power(a, n ):
    if n == 0:
        return 1
    elif n < 0:
        return 1.0 / a * power(a, n + 1)
    else:
        return a * power(a, n-1)

base = int(input("Base nuber: "))
powering = int(input("Power number: "))
print(power(base, powering))

