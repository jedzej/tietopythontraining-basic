# reverse_the_sequence.py


def print_reverse(number=1):
    if number != 0:
        nr = int(input("give number: "))
        print_reverse(nr)
        print(nr)


print_reverse()
