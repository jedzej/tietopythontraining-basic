def main():
    inspect_args(1, 2, 3, fourth='4', fifth='5')


def inspect_args(*args, **kwargs):
    item = 0
    for elem in args:
        print("  args param {0} is equal {1}".format(item, str(elem)))
        item += 1
    for key, value in kwargs.items():
        print("kwargs param {0} is equal {1}".format(key, str(value)))


if __name__ == '__main__':
    main()
