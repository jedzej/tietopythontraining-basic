#!/usr/bin/env python3


def greater_than_neighbours(list_in):
    count = 0
    num_of_elements = len(list_in)

    for i in range(1, num_of_elements - 1):
        if list_in[i] > list_in[i - 1] and list_in[i] > list_in[i + 1]:
            count += 1

    return count


def main():
    try:
        list_of_numbers = [int(i) for i in input(
            "Please enter numbers separated with spaces\n").split()]
    except ValueError:
        print("Something went wrong with your input, please try again")
        exit()

    print(greater_than_neighbours(list_of_numbers))


if __name__ == "__main__":
    main()
