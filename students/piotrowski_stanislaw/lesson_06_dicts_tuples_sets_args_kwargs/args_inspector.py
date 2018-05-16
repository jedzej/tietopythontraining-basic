# http://greenteapress.com/thinkpython2/html/thinkpython2020.html#sec231
# Args inspector - write a function called inspect_args that prints passed args and kwargs in human-readable format.
# piotrsta


def inspect_args(*args, **kwargs):
    print("Passed args:")
    for arg in args:
        print(arg)
    print("Passed kwargs:")
    for key, value in kwargs.items():
        print(value)


if __name__ == "__main__":
    inspect_args(1, 2.0, third='3')

# TO DO
# Input Validation
