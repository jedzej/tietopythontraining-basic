import math
startX = int(input("Give start x position: "))
startY = int(input("Give start y position: "))
endX = int(input("Give end x position: "))
endY = int(input("Give end y position: "))

if (abs(startX - endX) == 2 and abs(startY - endY) == 1) or (abs(startX
                                    - endX) == 1 and 2 == abs(startY - endY)):

    print("Yes")
else:
    print("No")
