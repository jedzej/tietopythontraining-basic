def reverse():
    x = int(input("Enter a number: "))
    if x != 0:
        reverse()
    print(x)


reverse()
