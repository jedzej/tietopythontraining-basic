def age_calculator(a):
    adults = [i for i in a if i >= 18]
    children = [i for i in a if i < 18]

    if len(adults) > 0:
        average_adults = sum(adults) / len(adults)
    else:
        average_adults = "no adults in the list"

    count_children = len(children)

    print("The average age of adults is:", average_adults)
    print("There are " + str(count_children) + " children")


def main():
    list_of_ages = [int(i) for i in input("Input list: ").split()]

    print(age_calculator(list_of_ages))


if __name__ == '__main__':
    main()
