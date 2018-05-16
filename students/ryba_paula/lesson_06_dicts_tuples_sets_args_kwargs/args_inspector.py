def inspect_args(*args, **kwargs):
    print("Args:")
    for arg in args:
        print(str(arg))

    print("Kwargs:")
    for key, val in kwargs.items():
        print("{0} : {1}".format(key, val))


def main():
    inspect_args(1, 2, 3, 4, **{'five': 5, 'six': 6})


if __name__ == '__main__':
    main()
