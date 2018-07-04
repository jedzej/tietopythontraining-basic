#!/usr/bin/env python3


from students.piechowski_michal.lesson_14_decorators.authorization import has_access


def access_required(func):

    def func_wrapper(string_arg):
        if has_access(string_arg):
            return func(string_arg)
        else:
            return None
    return func_wrapper


@access_required
def restricted_print(*args, **kwargs):
    print(*args, **kwargs)


def main():
    restricted_print('1 - visible')
    restricted_print('2 - invisible')
    restricted_print('3 - invisible')
    restricted_print('4 - visible')


if __name__ == "__main__":
    main()
