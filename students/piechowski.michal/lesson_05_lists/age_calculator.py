#!/usr/bin/env python3


def adult_filter(age):
    return age >= 18


people_age_list = [int(x) for x in input("Input the age list: ").split()]
adults_age_list = [int(x) for x in people_age_list if adult_filter(x)]
children_age_list = [int(x) for x in people_age_list if not adult_filter(x)]

age_sum = 0
counter = 0
for age in adults_age_list:
    age_sum += age
    counter += 1

print("Average age of adults: " + str(age_sum / counter))

age_sum = 0
counter = 0
for age in children_age_list:
    age_sum += age
    counter += 1

print("Average age of children: " + str(age_sum / counter))
