def exponentiation(value, to_the_power):
    if to_the_power == 0:
        return 1
    else:
        return value * exponentiation(value, to_the_power-1)

print(exponentiation(float(input("Type number: ")), int(input("To the power of: "))))