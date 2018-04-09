a = int(input())

largest = a
numbers_of_max = 1

while a != 0:
    a = int(input())
    if a == largest:
        numbers_of_max += 1
    elif a > largest:
        largest = a
        numbers_of_max = 1
print(numbers_of_max)
