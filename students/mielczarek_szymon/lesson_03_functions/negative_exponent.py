def power(a, n):
    ret = 1
    for i in range(abs(n)):
        ret *= a
    if n < 0:
        ret = 1 / ret
    return ret


print(power(float(input()), int(input())))
