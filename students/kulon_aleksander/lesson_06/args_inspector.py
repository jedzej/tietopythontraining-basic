def args_inspect(*args, **kwargs):
    for x in args:
        print(x)

    for k, v in kwargs.items():
        print(k, v)


def main():
    print(args_inspect(1, 2.0, third='3', fourth='4'))


if __name__ == "__main__":
    main()
