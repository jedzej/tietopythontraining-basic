def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total


def main():
    print(sum_all(1, 2, 3, 4, 5))


if __name__ == '__main__':
    main()
