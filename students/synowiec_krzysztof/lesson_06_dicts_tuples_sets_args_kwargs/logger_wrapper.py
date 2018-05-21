from args_inspector import args_inspector


def main():
    wrap_logs(do_nothing, 1, 2, 3, number="12345", email="lol@gmail.com")


def wrap_logs(foo, *args, **kwargs):
    args_inspector(*args, **kwargs)
    foo(args, kwargs)


def do_nothing(*args, **kwargs):
    print("I do nothing! :)")


if __name__ == '__main__':
    main()
