def sum_all(*args):
    result = 0
    for val in args:
        result += val
    return result


print(sum_all(3, 6, 0.5))
print(sum_all(0, 0))
