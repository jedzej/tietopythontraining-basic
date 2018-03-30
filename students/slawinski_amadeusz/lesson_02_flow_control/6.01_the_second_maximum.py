# find second to largest number in sequence of positive numbers ending with 0

largest = 0
second_to_largest = 0

while True:
    number = int(input())
    if number > largest:
        second_to_largest = largest
        largest = number
    elif number > second_to_largest:
        second_to_largest = number
    elif number == 0:
        break

print(second_to_largest)
