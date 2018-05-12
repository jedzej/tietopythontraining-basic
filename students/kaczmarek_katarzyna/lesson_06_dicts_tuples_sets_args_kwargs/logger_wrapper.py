from args_inspector import args_inspector


def logger_wrapper(foo, *args, **kwargs):
    args_inspector(*args, **kwargs)
    foo(*args, **kwargs)


def dummy_function(*args, **kwargs):
    print("\nInside dummy function")
    print("Number of args: " + str(len(args)))
    print("Number of kwargs: " + str(len(list(kwargs))))


def main():
    logger_wrapper(dummy_function, "Wrocław", 28,
                   firstName="Katarzyna", lastName="Kaczmarek")


if __name__ == '__main__':
    main()
