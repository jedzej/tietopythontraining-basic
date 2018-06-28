# logger_wrapper.py

from args_inspector import args_inspector


def logger_wrapper(foo, *args, **kwargs):
    """
    Examples
    --------
    args = [0, 2, "a"]
    kwargs = {'aa': 0, 'bb': 'qq', 'cc': 1.}

    # 2 times result of  args_inspector(*args, **kwargs):
    logger_wrapper(args_inspector, *args, **kwargs)

    def foo(a, b, c, d, e):
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)

    logger_wrapper(foo, *[1, 2], **{'c': 'c', 'd': 'd', 'e': 'e'})
        args:
        1 : 1
        2 : 2
        kwargs:
        c : c
        d : d
        e : e
        1
        2
        c
        d
        e

    logger_wrapper(foo, *[1, 2], **{'a': 'a', 'd': 'd', 'e': 'e'})
        # ERROR, OK

    bar = foo
    logger_wrapper(bar, *[1, 2], **{'c': 'c', 'd': 'd', 'e': 'e'})
        # as for foo()
    """
    args_inspector(*args, **kwargs)

    print()

    foo(*args, **kwargs)
