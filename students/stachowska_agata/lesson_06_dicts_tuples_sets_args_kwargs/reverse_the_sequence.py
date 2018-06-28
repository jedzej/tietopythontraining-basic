def reverse_the_sequence():
    i = int(input())
    if i != 0:
        reverse_the_sequence()
    print(i)


reverse_the_sequence()
