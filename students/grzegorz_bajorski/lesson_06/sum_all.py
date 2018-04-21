def sum_all(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(sum_all(1, 2, 3))
