def age_calculator(age_of_people):
    adults_age = [i for i in age_of_people if i >= 18]
    average_adults_age = sum(adults_age) / len(adults_age)
    j = 0
    count_children = sum([j + 1 for i in age_of_people if i < 18])
    return average_adults_age, count_children


age_list = [1, 40, 30, 12, 3, 35, 4, 25, 20]
adult, children = age_calculator(age_list)
print("Adult Average: " + str(adult))
print("Children Count: " + str(children))
