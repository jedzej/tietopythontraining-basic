def power(a, n):
    """Calculates real number a to the power of n (recursive solution)

    Arguments:
    a -- positive real number
    n -- non-negative integer
    """
    if n == 0:
        return 1
    return a * power(a, n - 1)


def main():
    # read positive real number a and it's non-negative power n
    a = float(input())
    n = int(input())
    # calculate n to the power of p
    print(power(a, n))


if __name__ == '__main__':
    main()
