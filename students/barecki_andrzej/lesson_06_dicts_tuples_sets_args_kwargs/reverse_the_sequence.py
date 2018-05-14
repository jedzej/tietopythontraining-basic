def reverse_sequence():
    """"remember input value"""
    input_integer = int(input())
    """"is it end of the sequence"""
    if input_integer != 0:
        """"check next value"""
        reverse_sequence()
    print(input_integer)


reverse_sequence()
