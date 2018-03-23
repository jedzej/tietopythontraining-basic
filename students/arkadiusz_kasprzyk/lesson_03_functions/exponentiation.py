def power(a, n):

    if n < 0:
        a = 1 / a
        n = -n
        return power(a, n)
    elif n > 0:
        return a * power(a, n - 1)
    else:
        return 1


print("Calculates a^n (a to the power of n).")

a = float(input("Give a: "))
n = int(input("Give n: "))

print(power(a, n))
