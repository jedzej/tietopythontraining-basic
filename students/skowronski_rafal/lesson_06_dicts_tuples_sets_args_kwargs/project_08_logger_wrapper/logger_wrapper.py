def print_arguments(*args, **kwargs):
    """Prints '*args' and '**kwargs' in human readable form.

    Args:
        *args: Variable length arguments.
        **kwargs: Variable length keyword arguments.
    """

    args_string = ', '.join(['{0!r}'.format(i) for i in args])
    print('Positional arguments:')
    print(args_string)

    print()

    kwargs_string = ', '.join(
        '{0}={1!r}'.format(k, v) for k, v in kwargs.items())
    print('Keyword arguments:')
    print(kwargs_string)


def logger_wrapper(foo, *args, **kwargs):
    """Logs arguments passed to function."""

    print_arguments(*args, **kwargs)
    foo(*args, **kwargs)


if __name__ == '__main__':
    def buz(a, b, c, d, e):
        print('In buz() function')

    buz(1, 2, 3, d=12, e=11)
    logger_wrapper(buz, 1, 2, 3, d=12, e=11)
