def sum_args(*args):
    total = 0
    for arg in args:
        total += arg
    return total


if __name__ == '__main__':
    print(sum_args(1, 2, 3, 4))
