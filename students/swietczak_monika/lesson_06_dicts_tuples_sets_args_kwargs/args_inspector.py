def print_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg_key, kwarg_value in kwargs.items():
        print('{}={}'.format(kwarg_key, kwarg_value))


print_all(1, "test", [1, 3], first_name="Monika", last_name="Sw")
