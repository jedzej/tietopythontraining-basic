def sequence():
    x = int(input())
    if x != 0:
        sequence()
    print(x)


sequence()
