def reverse_the_sequence():
    entry = int(input())
    if entry != 0:
        reverse_the_sequence()
    print(entry)


reverse_the_sequence()
