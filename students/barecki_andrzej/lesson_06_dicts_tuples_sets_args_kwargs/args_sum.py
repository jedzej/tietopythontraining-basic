def main():

    print(sum_all(1))
    print(sum_all(1, 2))
    print(sum_all(1, 2, 3))
    print(sum_all(1, 2, 3, 4))
    print(sum_all(1, 2, 3, 4, 5))
    print(sum_all(1, 2, 3, 4, 5, 6))


def sum_all(*args):
    total_sum = 0
    for elem in args:
        total_sum += elem
    return total_sum


if __name__ == '__main__':
    main()
