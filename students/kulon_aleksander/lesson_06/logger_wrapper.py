from lesson_06.args_inspector import args_inspect


def log_wrapper(fun, *args, **kwargs):
    return fun(args, kwargs)


def main():
    print(log_wrapper(args_inspect, 1, 2.0, third='3', fourth='4'))


if __name__ == "__main__":
    main()
