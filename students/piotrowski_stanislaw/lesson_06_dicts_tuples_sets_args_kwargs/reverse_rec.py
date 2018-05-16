# https://snakify.org/lessons/functions/problems/reverse_rec/
# Reverse the sequence
# piotrsta


def reverse_sequence():
    num = int(input('Enter the integer. (The number zero ends) :'))
    if num != 0:
        reverse_sequence()
    print(num)


if __name__ == "__main__":
    reverse_sequence()

# TO DO
# Input Validation
