def recursion_revers(int_val):
    if int_val == 0:
        print(int_val)
        return 0
    recursion_revers(int(input()))
    print(int_val)


recursion_revers(int(input()))
