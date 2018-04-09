
def determine_number_of_elements_equal_to_the_maximum():

    maximum = 0
    num_maximal = 0
    element = -1

    while element != 0:
        element = int(input())
        if element > maximum:
            maximum, num_maximal = element, 1
        elif element == maximum:
            num_maximal += 1

    print(num_maximal)


determine_number_of_elements_equal_to_the_maximum()
