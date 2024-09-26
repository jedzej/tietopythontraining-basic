def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)


reverse()
