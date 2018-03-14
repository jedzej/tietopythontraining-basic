import math

startX = int(input())
startY = int(input())
endX = int(input())
endY = int(input())

moveX = startX - endX
moveY = startY - endY

result = 'NO'
if (math.fabs(moveX) == 2 and math.fabs(moveY) == 1) or (math.fabs(moveY) == 2 and math.fabs(moveX) == 1):
    result = 'YES'

print("Is move possible: "+result)
