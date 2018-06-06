def inspect_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)


def main():
    print(inspect_args(1, 3.0, 7, 9))


if __name__ == "__main__":
    main()
