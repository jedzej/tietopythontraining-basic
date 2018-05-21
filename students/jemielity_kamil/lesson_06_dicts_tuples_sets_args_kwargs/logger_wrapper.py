from students.jemielity_kamil.lesson_06_dicts_tuples_sets_args_kwargs \
    .args_inspector import inspect_args


def special_function(*args, **kwargs):
    print()
    print('***** Special function *****')
    print('Args: ' + str(args))
    print('Kwargs: ' + str(kwargs))


def logger_wrapper(foo, *args, **kwargs):
    inspect_args(*args, **kwargs)
    foo(*args, **kwargs)


if __name__ == "__main__":
    logger_wrapper(special_function, 1, 2, 3, [1, 2, 3], (1, 2, 3),
                   kwarg="String1", kwarg2="String1", list=[1, 2, 3])
