
def power(a, n):

    result = 1

    for i in range(abs(n)):
        result *= a
    if n >= 0:
        return result
    else:
        return 1 / result


a_input, n_input = float(input("Provide a ")), int(input("Provide n "))

if __name__ == '__main__':
    print(power(a_input, n_input))
