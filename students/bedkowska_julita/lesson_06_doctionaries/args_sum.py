def sum_all(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(sum_all(2, 4, 5))
print(sum_all(1, 0, 9, 10, 10))
