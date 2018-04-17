def power(a, n):
    res = 1
    for x in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


if __name__ == "__main__":
    print(power(float(input()), int(input())))
