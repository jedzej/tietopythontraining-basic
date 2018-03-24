largest = 0
second_largest = 0

while True:
    number = int(input("Type a positive integer number. "
                       "0 ends the program. Number: "))
    if number == 0:
        break
    if number > largest:
        second_largest, largest = largest, number
    elif second_largest < number < largest:
        second_largest = number

print(second_largest)
