def get_how_many_elements_are_equal_to_largest_element():
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


if __name__ == '__main__':
    get_how_many_elements_are_equal_to_largest_element()
