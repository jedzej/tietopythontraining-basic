
def inspect_args(*args, **kwargs):

    for i, arg in enumerate(args):
        print("Arg {}: {}".format(str(i + 1), str(arg)))

    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))


if __name__ == '__main__':
    inspect_args(1, 2, '1')
