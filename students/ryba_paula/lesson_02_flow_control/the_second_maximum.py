largest = 0
second_largest = 0

while True:
    number = int(input())
    if number == 0:
        break
    if number > largest:
        second_largest, largest = largest, number
    elif number > second_largest and number < largest:
        second_largest = number

print(second_largest)
