def average_age(people_list):
    age_sum = 0
    for row in people_list:
        age_sum += row
    return age_sum / int(len(people_list))


list_of_peoples_ages = [int(x) for x in input().split()]
adults_list = [x for x in list_of_peoples_ages if x >= 18]
children_list = [x for x in list_of_peoples_ages if x < 18]
print("Adult avg age: {0}".format(average_age(adults_list)))
print("Children count: {0}".format(len(children_list)))
