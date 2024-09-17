# http://greenteapress.com/thinkpython2/html/thinkpython2013.html#sec144
# Args sum - write a function called sum_all that takes any number of arguments and returns their sum.
# piotrsta


def sum_all(*args):
    sum_args = 0
    for arg in args:
        sum_args += arg
    return sum_args


if __name__ == "__main__":
    print(sum_all(34, 43, 435, 7645, 45))

# TO DO
# Input Validation
