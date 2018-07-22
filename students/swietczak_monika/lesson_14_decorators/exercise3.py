def logger_wrapper(foo, *args, **kwargs):
    print("Args: ")
    for arg in args:
        print(str(arg))

    print("Kwargs: ")
    for key, value in kwargs.items():
        print("{} : {}".format(key, value))

    foo(*args, **kwargs)


def logged(some_function):
    def wrapper(*args, **kwargs):
        # ("logger wrapper for function")
        logger_wrapper(some_function, *args, **kwargs)

        # print("Something after some_function() is called")

    return wrapper


@logged
def just_some_function(*args, **kwargs):
    print("Just some function with args: {}, kwargs: {}".format(args, kwargs))


@logged
def add_some_numbers(number_one, number_two):
    print("Numbers added=", str(number_one + number_two))


@logged
def no_args_function():
    print("No args function!")


def main():
    some_dict = {'c': 2, 'd': 3}
    just_some_function("a", "b", **some_dict)
    just_some_function("a", "b")
    just_some_function(**some_dict)
    just_some_function()
    add_some_numbers(1, 2)
    no_args_function()


if __name__ == "__main__":
    main()
