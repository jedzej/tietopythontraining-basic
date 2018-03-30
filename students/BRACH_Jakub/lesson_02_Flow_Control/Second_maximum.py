maximum = 0
second_best = 0
while 1:
    data = int(input())
    if data == 0:
        break
    if data >= maximum:
        second_best = maximum
        maximum = data
    elif data > second_best:
        second_best = data
print(second_best)
