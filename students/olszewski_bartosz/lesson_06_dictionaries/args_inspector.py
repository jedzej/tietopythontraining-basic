def inspect_args(*args, **kwargs):
    for arg in args:
        print(str(arg), end='. ')
    for key, value in kwargs.items():
        print(str(key) + " to " + str(value), end=',\n')


inspect_args(1, Motor="Lublin", Hetman="Zamość")
inspect_args(2, Jeziorak="Iława", Roztocze="Szczebrzeszyn")
