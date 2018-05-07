def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


def main():
    print(power(float(input()), int(input())))


if __name__ == "__main__":
    main()
