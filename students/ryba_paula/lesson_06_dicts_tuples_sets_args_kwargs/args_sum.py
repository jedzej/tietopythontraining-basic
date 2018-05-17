def args_sum(*args):
    a_sum = 0
    for i in args:
        a_sum += i
    return a_sum


def main():
    print(args_sum(1, 2, 4))


if __name__ == '__main__':
    main()
