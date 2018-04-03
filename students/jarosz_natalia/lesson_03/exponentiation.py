def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


def main():
    print(power(float(input()), int(input())))


if __name__ == '__main__':
    main()
