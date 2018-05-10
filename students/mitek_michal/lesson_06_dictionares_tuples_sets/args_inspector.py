
def inspect_args(*args, **kwargs):

    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))


if __name__ == '__main__':
    inspect_args()
