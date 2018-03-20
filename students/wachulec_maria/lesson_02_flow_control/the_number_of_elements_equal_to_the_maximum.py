number = int(input("Number: "))
large_number = number
sum_of_large_number = 1
while True:
    number = int(input("Number: "))
    if number > large_number:
        large_number = number
        sum_of_large_number = 1
    elif number == large_number:
        sum_of_large_number += 1
    if number == 0:
        print(sum_of_large_number)
        break
