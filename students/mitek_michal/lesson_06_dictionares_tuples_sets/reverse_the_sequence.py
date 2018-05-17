
def reverse_the_sequence():

    number = int(input())

    if number != 0:
        reverse_the_sequence()

    print(number)


if __name__ == '__main__':
    reverse_the_sequence()
