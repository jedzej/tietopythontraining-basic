def age_calculator(ages):
    adults = [age for age in ages if age >= 18]
    children = [age for age in ages if age < 18]

    adults_average = 0
    for x in adults:
        adults_average += x

    adults_average = adults_average / len(adults)
    return adults_average, len(children)


if __name__ == "__main__":
    people_ages = [10, 20, 30, 2, 3, 5, 8, 11, 99]
    average, children_counter = age_calculator(people_ages)
    print("Average of adults age: " + str(average))
    print("Number of children: " + str(children_counter))
