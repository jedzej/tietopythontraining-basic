largest = 0
count = 0
while True:
    number = int(input())
    if number != 0:
        if number > largest:
            largest = number
            count = 1
        elif number == largest:
            count += 1
    else:
        break
print(count)
