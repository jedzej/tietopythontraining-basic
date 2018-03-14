import math

startX = int(input())
startY = int(input())
endX = int(input())
endY = int(input())

moveX = startX - endX
moveY = startY - endY

result = 'NO'
if math.fabs(moveX) == math.fabs(moveY):
    result = 'YES'

print("Is move possible: "+result)
