def power(a, n):
    if a == 0:
        return 0
    elif n == 1:
        return a
    elif n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print ("Compute a^n")
print ("Give base: ")
base = float(input())
print ("Give exponent: ")
exponent = float(input())
print(power(base, exponent))
