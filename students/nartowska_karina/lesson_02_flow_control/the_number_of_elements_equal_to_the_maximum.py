numbers = []
tmp = -1
max_value = 0
while tmp != 0:
    tmp = int(input())
    if tmp >= max_value:
        max_value = tmp
        numbers.append(tmp)
print(numbers.count(max_value))
