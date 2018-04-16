def reverse_the_sequence():
    number = int(input('Value: '))
    if number != 0:
        reverse_the_sequence()
    print(number)


reverse_the_sequence()
