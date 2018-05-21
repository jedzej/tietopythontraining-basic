def inspect_args(*args, **kwargs):
    print("***** List of arguments: ******")

    for counter, arg in enumerate(args, start=1):
        print("Argument " + str(counter) + ": " + str(arg))

    print()
    print("***** List of kwargs: ******")

    for counter, (kwarg_key, kwarg_value) in enumerate(kwargs.items(),
                                                       start=1):
        print("Kwarg " + str(counter) + ": " + str(kwarg_key) +
              " value: " + str(kwarg_value))


if __name__ == "__main__":
    inspect_args(1, 2, 3, [1, 2, 3], (1, 2, 3), kwarg="String1",
                 kwarg2="String1", list=[1, 2, 3])
