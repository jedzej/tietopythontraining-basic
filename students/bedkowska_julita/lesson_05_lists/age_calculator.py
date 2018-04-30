list_of_ages = [12, 13, 61, 83, 20, 7, 45, 2]


def calculate_avg(list_of_ages):
    print('Given list of peoples ages: ' + str(list_of_ages))
    sum = 0
    num_of_adults = 0
    for i in range(len(list_of_ages)):
        age = list_of_ages[i]
        if age >= 18:
            sum += list_of_ages[i]
            num_of_adults += 1
    avg_age_of_adults = sum / num_of_adults
    print('Averge number of adults age: ' + str(avg_age_of_adults))
    num_of_children = len(list_of_ages) - num_of_adults
    print('Nuber of children: ' + str(num_of_children))


calculate_avg(list_of_ages)
