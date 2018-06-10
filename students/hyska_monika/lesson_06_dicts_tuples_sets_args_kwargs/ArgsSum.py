# Args sum - function sum_all takes any number of arguments
# and returns their sum.


def sum_all(*args):
    return sum(args)


print(sum_all(5, 4, 3))
print(sum_all(10, 5))
print(sum_all(5, 4, 3, 9, 66))
print(sum_all())
print(sum_all(10))
