def inspect_args(*args, **kwargs):
    for i in args:
        print(i)

    for key, val in kwargs.items():
        print(key, val)


def main():
    print(inspect_args(2.5, 5, 6, 1, 9, kwarg1='1', kwarg2='2'))


if __name__ == '__main__':
    main()
