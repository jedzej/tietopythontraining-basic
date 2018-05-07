def power(base, exponent):
    return base ** exponent


print("Compute a^n")
a = float(input("Give base: "))
n = int(input("Give exponent: "))
print(power(a, n))
