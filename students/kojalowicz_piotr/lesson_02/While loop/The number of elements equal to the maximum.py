integer= int(input())
integerMax = integer
count = 0
while integer != 0:
    if integerMax < integer:
        integerMax = integer
        count = 0
    if integerMax == integer:
        count += 1
    integer = int(input())
print(count)