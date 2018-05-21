def inspect_args(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print('{} : {}'.format(key, value))


def main():
    inspect_args('1', 2, '3', arg1=1, arg2='uaha', arg3='golf2')


if __name__ == '__main__':
    main()
