def power(a, n):
    result = 1
    if n >= 0:
        for i in range(1, n + 1):
            result = result * a
    else:
        for i in range(n, 0):
            result = result / a
    return result


def main():
    a = float(input())
    n = int(input())

    print(power(a, n))


if __name__ == '__main__':
    # `python hello_world.py` will run main(), `import hello_world` will not
    main()
