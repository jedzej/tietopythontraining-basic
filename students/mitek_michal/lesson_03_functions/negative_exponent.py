
def power(a, n):

    result = 1

    for i in range(abs(n)):
        result *= a
    if n >= 0:
        return result
    else:
        return 1 / result


if __name__ == '__main__':
    a_input, n_input = float(input("Provide a ")), int(input("Provide n "))
    print(power(a_input, n_input))
