maximum = 0
last_number = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, last_number = element, 1
    elif element == maximum:
        last_number += 1
print(last_number)
