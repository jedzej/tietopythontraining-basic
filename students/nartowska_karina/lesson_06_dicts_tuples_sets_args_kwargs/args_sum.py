def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def main():
    print("Result:")
    print(sum_all(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))


if __name__ == '__main__':
    main()
