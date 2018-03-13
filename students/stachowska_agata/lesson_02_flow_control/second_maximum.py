second_max = 0
first_max = 0
while True:
    number = int(input())
    if number != 0:
        if number > first_max:
            second_max = first_max
            first_max = number
        elif number > second_max:
            second_max = number
    else:
        break
print(second_max)
