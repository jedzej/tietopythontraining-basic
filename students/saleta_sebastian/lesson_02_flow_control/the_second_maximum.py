def find_second_maximum():
    first_maximum = int(input())
    second_maximum = int(input())

    if first_maximum < second_maximum:
        first_maximum, second_maximum = second_maximum, first_maximum

    element = int(input())

    while element != 0:
            if element > first_maximum:
                second_maximum, first_maximum = first_maximum, element
            elif element > second_maximum:
                second_maximum = element
            element = int(input())

    print(second_maximum)

if __name__ == '__main__':
    find_second_maximum()
