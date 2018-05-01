def inspect_args(*args, **kwargs):
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


if __name__ == '__main__':
    inspect_args(1, 2, 3, 'a', k='12', c='11', d=111)
