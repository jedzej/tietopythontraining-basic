#!/usr/bin/env python3


from students.piechowski_michal.lesson_06_dicts_tuples_sets_args_kwargs.logger_wrapper import logger_wrapper


def logged(func):

    def func_wrapper(*args, **kwargs):
        logger_wrapper(func, *args, **kwargs)
    return func_wrapper


@logged
def foo(*args, **kwargs):
    print("foo function")


@logged
def bar(some_arg):
    print("bar function: " + str(some_arg))


@logged
def kar():
    print("kar function without arguments")


def main():
    print("CHECKING foo without arguments:")
    foo()

    print("\n\nCHECKING foo with arguments:")
    foo("some", "interesting", arguments=[2, 7, 3])

    print("\n\nCHECKING bar with some argument:")
    bar("text")

    print("\n\nCHECKING kar without arguments:")
    kar()


if __name__ == "__main__":
    main()
