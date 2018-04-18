# args_inspector.py

def args_inspector(*args, **kwargs):
    """
    Examples
    --------
    args = [0, 2, "a"]
    kwargs = {'aa':0, 'bb':'qq', 'cc':1.}
    args_inspector(*args, **kwargs)
    """
    k = 0
    print("args:")
    for arg in args:
        k += 1
        print("{} : {}".format(k, arg))

    print("\nkwargs:")
    #print(kwargs)
    for arg in kwargs:
        print("{} : {}".format(arg, kwargs[arg]))
