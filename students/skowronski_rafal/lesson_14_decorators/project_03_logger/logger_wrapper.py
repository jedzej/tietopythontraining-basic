'''Reviewed version of logger_wrapper.py from lesson 6'''


def _get_arguments_string(*args, **kwargs):
    return ', '.join(
        ['{0!r}'.format(i) for i in args] +
        ['{0}={1!r}'.format(k, v) for k, v in kwargs.items()]
    )


def logger_wrapper(foo, *args, **kwargs):
    print('--log: {0}({1})'
          .format(foo.__name__, _get_arguments_string(*args, **kwargs)))
    foo(*args, **kwargs)


if __name__ == '__main__':
    def buz(a, b, c, d, e):
        print('In buz() function')

    buz(1, 2, 3, d=12, e=11)
    logger_wrapper(buz, 1, 2, 3, d=12, e=11)
