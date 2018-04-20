def example_function(*args, **kwargs):
    print("\nArgs & Kwargs provided for called function:")
    summary = 0
    for argument in args:
        summary += argument
        print(argument)
    print("\nKey =>  Value")
    for key in kwargs:
        print(key, "=>", kwargs[key])
    return summary


def logger_wrapper(function_to_be_called, *args, **kwargs):
    print("Logger wrapper: ")
    print("Arguments captured by Logger_wrapper:")
    for argument in args:
        print(argument)
    print("\nKwargs captured by Logger wrapper:")
    for key in kwargs:
        print(key, "==>", kwargs[key])
    print("\nResult : ", function_to_be_called(*args, **kwargs))


def main():
    logger_wrapper(example_function, 2, 6, 30, 13, brand="Volkswagen",
                   car="Polo", year=2002, power=105)


if __name__ == "__main__":
    main()
