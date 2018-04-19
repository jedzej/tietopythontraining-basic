# logger_wrapper.pl

from args_inspector import args_inspector


def logger_wrapper(foo, *args, **kwargs):
    """
    args = [0, 2, "a"]
    kwargs = {'aa': 0, 'bb': 'qq', 'cc': 1.}
    logger_wrapper(args_inspector, *args, **kwargs)

    def foo(a, b, c, d, e):
        for par in [a, b, c, d, e]:
            print(par)

    logger_wrapper(foo, *[1, 2], **{'c': 'c', 'd': 'd', 'e': 'e'})
    logger_wrapper(foo, *[1, 2], **{'a': 'a', 'd': 'd', 'e': 'e'})  # ERROR
    """
    args_inspector(*args, **kwargs)

    print()

    foo(*args, **kwargs)
