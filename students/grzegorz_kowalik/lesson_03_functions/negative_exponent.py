def pow(x, a):
    if a < 0:
        x = 1 / x
        a = -a
    res = 1
    for _ in range(0, a):
        res *= x
    return res


print(pow(float(input("x: ")), int(input("a: "))))
