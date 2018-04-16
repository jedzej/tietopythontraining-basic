def power(x, n):
    t = n
    if t < 0:
        t = -t
    val = 1
    for i in range(1, t + 1):
        if n > 0:
            val = val * x
        elif n < 0:
            val = val / x
    return val


def main():
    x = float(input())
    n = int(input())

    result = power(x, n)
    print(result)


if __name__ == '__main__':
    main()
