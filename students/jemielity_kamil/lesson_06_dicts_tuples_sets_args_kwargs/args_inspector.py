def inspect_args(*args, **kwargs):
    print("***** List of arguments: ******")
    counter = 1
    for arg in args:
        print("Argument " + str(counter) + ": " + str(arg))
        counter += 1

    print()
    print("***** List of kwargs: ******")
    counter = 1
    for kwarg_key, kwarg_value in kwargs.items():
        print("Kwarg " + str(counter) + ": " + str(kwarg_key) + " value: " + str(kwarg_value))
        counter += 1


if __name__ == "__main__":
    inspect_args(1, 2, 3, [1, 2, 3], (1, 2, 3), kwarg="String1",
                 kwarg2="String1", list=[1, 2, 3])
