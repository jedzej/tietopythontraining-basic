# Given a list of numbers, determine and print the quantity of elemets that
# are greater than both of their neighbors. The first and the last items of
# the list shouldn't be considered because they don't have two neighbors.


def greater_than_neighbours(list_value):
    if len(list_value) <= 2:
        return 0
    else:
        quantity = 0
        for i in range(1, len(list_value)-1):
            if int(list_value[i]) > int(list_value[i-1]) and \
                    int(list_value[i]) > int(list_value[i+1]):
                quantity += 1

    return quantity


def main():
    test = [-9, 29, -100, 64, 26, 73, -96, 28, -92, 11, -14, -86, -54, -67]
    print("quantity: " + str(greater_than_neighbours(test)))

    test = [1, 5, 1, 5, 1]
    print("quantity: " + str(greater_than_neighbours(test)))


if __name__ == "__main__":
    main()
