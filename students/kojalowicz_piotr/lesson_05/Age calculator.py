list_of_ages = [34, 56, 14, 16, 19]


def age_calculator(list_of_ages=[]):
    list_of_adults = []
    numer_of_kids = 0
    resalts = []
    for person in list_of_ages:
        if person < 18:
            numer_of_kids += 1
        else:
            list_of_adults.append(person)
    average_age_of_adults = sum(list_of_adults) / len(list_of_adults)
    resalts.append(average_age_of_adults)
    resalts.append(numer_of_kids)
    return resalts


print("Average of age is " + str(age_calculator(list_of_ages)[0]))
print("Number od kids is " + str(age_calculator(list_of_ages)[1]))
