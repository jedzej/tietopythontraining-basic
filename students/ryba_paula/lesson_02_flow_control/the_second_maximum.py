largest, second_largest = int(input()), int(input())

if largest < second_largest:
    largest, second_largest = second_largest, largest
    
number = int(input())

while number != 0:
    if number > largest:
        second_largest, largest = largest, number
    elif number > second_largest:
        second_largest = number
    number = int(input())
    
print(second_largest)