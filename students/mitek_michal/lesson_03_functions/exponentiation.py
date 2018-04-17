
def power(a, n):

    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


if __name__ == '__main__':
    a_input, n_input = float(input("Provide a ")), int(input("Provide n "))
    print(power(a_input, n_input))
