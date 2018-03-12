number = int(input())

largest = number
second_largest = 0

while number != 0:
    number = int(input())
    if number > largest:
        second_largest, largest = largest, number
    elif number > second_largest:
        second_largest = number

print(second_largest)
