from functools import reduce


def age_calculator():

    people_age = [12, 2, 3, 18, 32, 45, 52, 13, 8, 26]

    adults_age_list = [adult for adult in people_age if adult >= 18]
    average_adults_age = \
        reduce(lambda x, y: x + y, adults_age_list) / len(adults_age_list)

    children_list = [children for children in people_age if children < 18]

    print(len(children_list))
    print(average_adults_age)


if __name__ == '__main__':
    age_calculator()
