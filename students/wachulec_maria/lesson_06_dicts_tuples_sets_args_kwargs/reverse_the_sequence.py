def reverse_the_sequence():
    a = input()
    if a != '0':
        reverse_the_sequence()
    print(a)


reverse_the_sequence()
