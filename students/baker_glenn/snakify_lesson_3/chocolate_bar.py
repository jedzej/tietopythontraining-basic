# script to determine if a rectangle can be split into two regular parts
# by breaking it along a given size
print("enter the width of the chocoalte bar")
width = int(input())
print("enter the length of the chocoalte bar")
length = int(input())
print("enter the desired size to break it into")
new_block = int(input())

if new_block < (width * length):
    if ((new_block % width) == 0) or ((new_block % length) == 0):
        print("yes")
    else:
        print("no")
else:
    print("no")
