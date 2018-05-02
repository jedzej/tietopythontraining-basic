def sum_all(*args):
    sum = 0
    for i in range(len(args)):
        if type(args[i]) is str:
            sum = ''
            for j in range(len(args)):
                sum += str(args[j])
            return sum
    for i in range(len(args)):
        sum += args[i]
    return sum


print(sum_all('a', 1, 2, '2', 3))
print(sum_all(1, 2, 3))
print(sum_all(1, 3, 5, 's'))
print(sum_all(1, 2, 3, 4, 5))
