print("enter a number")
number = int(input())
max_number = number
second_max = 0
while number != 0:
    print("enter a number")
    number = int(input())
    if number > max_number:
        second_max = max_number
        max_number = number

    elif (number > second_max):
        second_max = number

print(second_max)
