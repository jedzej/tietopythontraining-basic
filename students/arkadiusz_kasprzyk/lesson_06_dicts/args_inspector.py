# args_inspector.py


def args_inspector(*args, **kwargs):
    """
    Examples
    --------
    args = [0, 2, "a"]
    kwargs = {'aa':0, 'bb':'qq', 'cc':1.}
    args_inspector(*args, **kwargs)
<<<<<<< HEAD

        args:
        1 : 0
        2 : 2
        3 : a

        kwargs:
        aa : 0
        bb : qq
        cc : 1.0
=======
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736
    """
    k = 0
    print("args:")
    for arg in args:
        k += 1
        print("{} : {}".format(k, arg))

    print("\nkwargs:")

    # print(kwargs)
    for arg in kwargs:
        print("{} : {}".format(arg, kwargs[arg]))
