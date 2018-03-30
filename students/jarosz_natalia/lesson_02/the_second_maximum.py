max1 = int(input())
max2 = int(input())

if max1 < max2:
    max1, max2 = max2, max1
element = int(input())
while element != 0:
    if element > max1:
        max2, max1 = max1, element
    elif element > max2:
        max2 = element
    element = int(input())
print(max2)
