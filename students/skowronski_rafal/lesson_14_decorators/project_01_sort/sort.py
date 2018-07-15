
def sort(func):
    def function_wrapper(*args):
        return sorted(func(*args))
    return function_wrapper


@sort
def to_list(*args):
    return [x for x in args]


if __name__ == '__main__':
    print(to_list(1, 11, 7, -22))
