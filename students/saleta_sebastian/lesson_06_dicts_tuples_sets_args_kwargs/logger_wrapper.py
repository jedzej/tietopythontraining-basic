def inspect_args(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print('{} : {}'.format(key, value))


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


def sum_the_args_and_add_to_kwargs(*args, **kwargs):
    summary = 0
    for arg in args:
        summary += arg
    print('summary: {}'.format(summary))
    kwarg = {'sum': summary}
    kwargs.update(kwarg)
    print(kwargs)


def main():
    logger_wrapper(sum_the_args_and_add_to_kwargs, 1, 2, 3, arg1=1,
                   arg2='uaha', arg3='golf2')


if __name__ == '__main__':
    main()
