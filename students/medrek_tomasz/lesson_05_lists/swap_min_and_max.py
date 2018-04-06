#!/usr/bin/env python3


def swap_min_and_max(list_in):
    max_el = min_el = list_in[0]

    for element in list_in:
        if element > max_el:
            max_el = element
        elif element < min_el:
            min_el = element

    for i, element in enumerate(list_in):
        if element == max_el:
            list_in[i] = min_el
        elif element == min_el:
            list_in[i] = max_el

    return list_in


def main():
    try:
        list_of_numbers = [int(i) for i in input(
            "Please enter integer numbers separated with spaces\n").split()]
    except ValueError:
        print("Something went wrong with your input, please try again")
        exit()

    print(*swap_min_and_max(list_of_numbers))


if __name__ == "__main__":
    main()
