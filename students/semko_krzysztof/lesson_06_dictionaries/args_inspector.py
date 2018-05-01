"""
Args inspector - write a function called inspect_args
that prints passed args and kwargs in human-readable format.
"""


def args_inspector(*args, **kwargs):
    print("*args:")
    for i in args:
        print(i)
    print("**kwargs:")
    for key, val in kwargs.items():
        print(str(key) + ": " + str(val))


def main():
    words = {'1':  'woops', '2': 'right'}
    args_inspector(1, 2, "hello", 'a', words, reverse=True, end='')


if __name__ == '__main__':
    main()
