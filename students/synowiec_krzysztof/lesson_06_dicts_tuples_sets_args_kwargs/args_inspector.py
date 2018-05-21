def main():
    args_inspector(1, 2, 3, country="Poland", city="Wroclaw")


def args_inspector(*args, **kwargs):
    print("Arguments:", end=" ")
    for value in args:
        print(value, end=" ")
    print("\n\nKey : Value pairs:")
    for key, value in kwargs.items():
        print("{0} : {1}".format(key, value))


if __name__ == '__main__':
    main()
