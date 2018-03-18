maximum = 0
count = 0
number = -1
while number != 0:
    number = int(input())
    if number > maximum:
        maximum, count = number, 1
    elif number == maximum:
        count += 1
print(count)
