def power(x, n):

    if n > 1:
        val = x * power(x, n - 1)
    else:
        return x
    return val


def main():
    x = float(input())
    n = int(input())

    result = power(x, n)
    print(result)


if __name__ == '__main__':
    main()
