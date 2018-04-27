def args_inspector(*args, **kwargs):
    print("Args:")
    for value in args:
        print(value)
    print("Kwargs:")
    print("Key - Value")
    for key, value in kwargs.items():
        print("{0} - {1}".format(key, value))


def main():
    print("Result:")
    args_inspector(1, name="Karina", surname="Nartowska")


if __name__ == '__main__':
    main()
