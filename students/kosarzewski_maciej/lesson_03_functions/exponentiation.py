def power(a, n):
    if a == 0:
        return 0
    elif n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print("Compute a^n")
base = float(input("Give base: "))
exponent = float(input("Give exponent: "))
print(power(base, exponent))
