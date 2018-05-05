def age_calculator(ages):
    adults = [age for age in ages if age >= 18]
    children = [age for age in ages if age < 18]

    if len(adults) > 0:
        avg_adults = sum(adults) / len(adults)
    else:
        avg_adults = "No adults"

    print("The average age of adults is: ", avg_adults)
    print("Number of children: " + str(len(children)))


def main():
    ages = [int(i) for i in input("Type list of people's ages "
                                  "(space separated):  ").split()]

    print(age_calculator(ages))


if __name__ == '__main__':
    main()
