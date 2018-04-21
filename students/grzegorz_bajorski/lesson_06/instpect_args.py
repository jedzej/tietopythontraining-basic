def inspect_args(*args, **kwargs):
    for arg in args:
        print(str(arg))
    for keyword, value in kwargs.items():
        print(str(keyword) + " " + str(value))


inspect_args(1, "string", [2, 3, 4], a = 1, b = 2, c = True)
