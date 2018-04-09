integer = int(input())
firstMax = 0
secendMax = 0
while integer != 0:
    if firstMax < integer:
        secendMax = firstMax
        firstMax = integer
    elif secendMax < integer:
        secendMax = integer
    integer = int(input())
print(secendMax)