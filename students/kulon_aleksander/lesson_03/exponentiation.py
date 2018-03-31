def power(a, n):
    if n == 0:
        return 1
    if n > 1:
        n = n - 1
        a = a * power(a, n)
        return a
    else:
        return a


def main():
    aa = float(input())
    nn = int(input())

    print(power(aa, nn))


if __name__ == '__main__':
    # `python hello_world.py` will run main(), `import hello_world` will not
    main()
