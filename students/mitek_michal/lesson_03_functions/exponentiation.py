
def power(a, n):

    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a_input, n_input = float(input("Provide a ")), int(input("Provide n "))

if __name__ == '__main__':
    print(power(a_input, n_input))
