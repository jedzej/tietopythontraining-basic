startX = int(input("Give start x position: "))
startY = int(input("Give start y position: "))
endX = int(input("Give end x position: "))
endY = int(input("Give end y position: "))

if endY == startY:
    print("No")
elif endX == startX:
    print("No")
else:
    print("Yes")
