
def determine_second_maximum():

    first_max = int(input("Provide first maximum "))
    second_max = int(input("Provide second maximum "))

    if first_max < second_max:
        first_max, second_max = second_max, first_max
    element = int(input())
    while element != 0:
        if element > first_max:
            second_max, first_max = first_max, element
        elif element > second_max:
            second_max = element
        element = int(input())

    print(second_max)


determine_second_maximum()
