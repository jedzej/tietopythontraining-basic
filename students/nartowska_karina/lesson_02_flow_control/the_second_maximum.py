numbers = []
tmp = -1
pos = 0
while tmp != 0:
    tmp = int(input())
    numbers.append(tmp)
    pos += 1
numbers.sort()
print(numbers[pos - 2])
