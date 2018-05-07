#!/usr/bin/env python3


def adult_filter(age):
    return age >= 18


people_age_list = [int(x) for x in input("Input the age list: ").split()]
adults_age_list = [x for x in people_age_list if adult_filter(x)]
children_age_list = [x for x in people_age_list if not adult_filter(x)]

if adults_age_list:
    average_age = sum(adults_age_list) / len(adults_age_list)
    print("Average age of adults: " + str(average_age))
else:
    print("There are no adults")

if children_age_list:
    average_age = sum(children_age_list) / len(children_age_list)
    print("Average age of children: " + str(average_age))
else:
    print("There are no children")
