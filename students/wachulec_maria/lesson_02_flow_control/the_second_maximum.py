base_1 = int(input("Number: "))
base_2 = int(input("Number: "))
while True:
    number = int(input("Number: "))
    if base_2 > base_1 and number > base_1:
        base_1 = number
    elif base_1 > base_2 and number > base_2:
        base_2 = number
    if base_1 > base_2:
        result = base_2
    else:
        result = base_1
    if number == 0:
        print(result)
        break
