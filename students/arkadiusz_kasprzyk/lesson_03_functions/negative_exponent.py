def power(a, n):

    if n < 0:
        a = 1 / a
        n = -n

    result = 1

    for k in range(n):
        result *= a

    return result


print("Calculates a^n (a to the power of n).")

a = float(input("Give a: "))
n = int(input("Give n: "))

print(power(a, n))
