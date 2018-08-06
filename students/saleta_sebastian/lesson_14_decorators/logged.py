def logger_wrapper(foo, *args, **kwargs):
    foo(*args, **kwargs)


def logged(func):
    def func_wrapper(*args, **kwargs):
        return logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def sum_the_args_and_add_to_kwargs(*args, **kwargs):
    summary = 0
    for arg in args:
        summary += arg
    print('summary: {}'.format(summary))
    kwarg = {'sum': summary}
    kwargs.update(kwarg)
    print(kwargs)


@logged
def print_text_with_hello(usr_text):
    print('hello ' + usr_text)


@logged
def print_args_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    if kwargs is not None:
        print(kwargs)


def main():
    sum_the_args_and_add_to_kwargs(1, 2, 3, arg1=1, arg2='uaha', arg3='golf2')
    print_text_with_hello('weltschmerz')
    print_args_kwargs('yasss')
    print_args_kwargs(arg1='wave')


if __name__ == '__main__':
    main()
