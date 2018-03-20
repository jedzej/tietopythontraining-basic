number = int(input())
numbers_list = []
a = 0
while number != 0:
    numbers_list.append(number)
    number = int(input())
    a += 1
numbers_list.sort()
print(numbers_list[a-2])
