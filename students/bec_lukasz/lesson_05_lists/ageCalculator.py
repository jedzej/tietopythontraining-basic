peoples_age = [12, 18, 22, 56, 45, 89, 2, 3, 4, 19]


def count_children(age_list):
    children = [i for i in age_list if i < 18]
    return len(children)


def count_adults_average(age_list):
    adults = [i for i in age_list if i >= 18]
    age_sum = 0
    for i in adults:
        age_sum += i
    return float(age_sum / len(adults))


print('There are ' + str(count_children(peoples_age)) + ' children')
print('Average age of adults is: ' + str(count_adults_average(peoples_age)))
