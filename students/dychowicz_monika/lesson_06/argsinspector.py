def args_inspector(*args, **kwargs):
    print("Passed arguments: ")
    for arg in args:
        print(arg)
    print("Passed keyword arguments: ")
    for k, v in kwargs.items():
        print("Keyword:", k, "| Value:", v)
    print()


if __name__ == "__main__":
    arguments_list = [1, 2.0, "arg3"]
    key_arguments = {"key_one": 1, "key_two": 2}
    args_inspector(*arguments_list, **key_arguments)
    args_inspector(3, 4.0, "test", right=True, left=2)
    args_inspector()