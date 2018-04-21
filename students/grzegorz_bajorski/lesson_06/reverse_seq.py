def print_reverse():
    number = int(input())
    if number != 0:
        print_reverse()
    print(number)


print_reverse()
