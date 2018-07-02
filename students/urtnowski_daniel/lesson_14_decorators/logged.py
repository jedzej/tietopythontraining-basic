#!/usr/bin/env python3

"""
logged.py: a practice project number 3 from:
Lesson 14 - Decorators

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


from lesson_06_dicts_tuples_sets_args_kwargs.args_and_kwargs import \
    logger_wrapper


def logged(fun):
    """
    This function is a decorator that wraps call to a function in order to log
    passed args.
    :param fun: reference to a function object
    """
    def wrapper(*args, **kwargs):
        return logger_wrapper(fun, *args, **kwargs)
    return wrapper


@logged
def any_params_fun(*args, **kwargs):
    print("received {} params".format(len(args) + len(kwargs)))


@logged
def single_param_fun(param):
    print("received object of type {}".format(type(param)))


@logged
def greeter():
    print("Hello!")


def main():
    any_params_fun(123, "some_str", ['one', 2, {'three': 3}], x=789.025)
    any_params_fun()
    any_params_fun(0)
    single_param_fun('some string')
    single_param_fun('')
    single_param_fun(3.14)
    greeter()


if __name__ == '__main__':
    main()
