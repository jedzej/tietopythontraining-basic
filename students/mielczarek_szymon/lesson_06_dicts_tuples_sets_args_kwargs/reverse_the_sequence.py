def reverse_order():
    i = int(input())
    if i != 0:
        reverse_order()
    print(i)


reverse_order()
