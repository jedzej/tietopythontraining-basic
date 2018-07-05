from args_inspector import inspect_args


def log_wrapper(fun, *args, **kwargs):
    return fun(args, kwargs)


def main():
    print(log_wrapper(inspect_args, 1, 2.0, third='3', fourth='4'))


if __name__ == "__main__":
    main()
