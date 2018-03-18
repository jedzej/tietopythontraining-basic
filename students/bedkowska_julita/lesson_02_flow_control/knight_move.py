import math

startX = int(input('Give the start column: '))
startY = int(input('Give the start row: '))
endX = int(input('Give the end column: '))
endY = int(input('Give the end row: '))

moveX = startX - endX
moveY = startY - endY

result = 'NO'
if (math.fabs(moveX) == 2 and math.fabs(moveY) == 1) or \
        (math.fabs(moveY) == 2 and math.fabs(moveX) == 1):
    result = 'YES'

if startX == endX and startY == endY:
    result = 'Destination is the same as the start position.'

print('{} {}'.format('Is move possible:', result))
