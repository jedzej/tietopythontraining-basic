#Args sum - write a function called sum_all that
#takes any number of arguments and returns their sum.


def sum_all(*args):

    res = 0
    for i in args:
        res = res + i
    return res


print(sum_all(-1, 0, 1, 2, 3.5))
print(sum_all(-1))
print(sum_all(-1, 1))
