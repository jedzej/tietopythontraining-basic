# Compute a^n where a - real number and n - integer number.


def power(a, n):
    if n < 0:
        a = 1 / a
        n = -n

    result = 1
    for i in range(n):
        # print(str(n))
        result *= a
    return result


a = float(input("Give a: "))
n = int(input("Give n: "))

print('Power(a, n) is: ' + str(float(power(a, n))))
