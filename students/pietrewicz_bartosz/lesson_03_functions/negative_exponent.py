def power(a, n):
    """Calculates real number a to the power of integer n"""
    if n == 0:
        res = 1
    else:
        res = a ** abs(n)
        if n < 0:
            res = 1 / res
    return res


def main():
    # Read real number a and it's integer exponent n
    a = float(input())
    n = int(input())
    # Print the result of a to the power of n
    print(power(a, n))


if __name__ == '__main__':
    main()
