def inspect_args(*args, **kwargs):
    print("Arguments:")
    for argument in args:
        print(argument)
    print("\nKey =>  Value")
    for key in kwargs:
        print(key, "=>", kwargs[key])


def main():
    inspect_args(2, 6, 30, car="Opel", year=2009, power=105)


if __name__ == "__main__":
    main()
