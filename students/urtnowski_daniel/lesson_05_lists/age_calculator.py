#!/usr/bin/env python3

"""
age_calculator.py: a practice project "Age calculator" from:
Lesson 5 - Lists + list comprehensions
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def age_calculator(age_list):
    """
    This function calculates for a given list of people's ages the average age
    of adults (age >= 18) and count the children (age < 18)
    :param age_list: a list of integers with people's ages
    :return [int, int]: average age of adults and count of children in input
    age list
    """
    children_count = sum([1 for age in age_list if age < 18])
    adults_age = [age for age in age_list if age >= 18]
    average_adults_age = sum(adults_age) / len(adults_age) if adults_age else 0

    return [average_adults_age, children_count]


def main():
    """
    This function defines a list  of people's ages, passes it to
    age_calculator() function and prints its result
    """
    age_list = [0, 1, 12, 100, 112, 60, 15, 8, 18, 19, 17, 3, 32, 25, 1]

    average_adults_age, children_count = age_calculator(age_list)
    print("average adults age: {}\nchildren count: {}"
          .format(average_adults_age, children_count))


if __name__ == '__main__':
    main()
