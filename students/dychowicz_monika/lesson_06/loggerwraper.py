def hello(name, right=True):
    print("Hello " + name + "!")
    print("right value:", right)


def logger_wrapper(foo, *args, **kwargs):
    print("Function will be called: ", foo.__name__,
          "(", ", ".join(args), ", ",
          ", ".join(f"{k} = {v}" for k, v in kwargs.items()), ")")
    # print(args, kwargs)
    foo(*args, **kwargs)
    print()


def empty_func():
    pass


if __name__ == "__main__":
    args_list = ["Bob"]
    kwargs_dict = {'right': False}
    kwargs_print = {'end': "!!!!"}
    logger_wrapper(hello, *args_list, **kwargs_dict)
    logger_wrapper(print, *args_list, **kwargs_print)
    logger_wrapper(empty_func)