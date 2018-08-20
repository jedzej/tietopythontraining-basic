# Args inspector - write a function called inspect_args
# that prints passed args and kwargs in human-readable format.


def inspect_args(*args, **kwargs):
    for a in args:
        print(a)

    for k, v in kwargs.items():
        print (k + ": " + str(v))


inspect_args(-1, 0, 1, 2, 3.5, city="Wroclaw", fruit="Apple", number=42)
