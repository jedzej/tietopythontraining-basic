# piotrsta
# Age calculator
# Write a program that for given list of people's ages
# calculate the average age of adults (age >= 18)
# and count the children (age < 18). Use list comprehensions.


def age_calculator(input_list):
    adult_ages_list = [int(x) for x in input_list if 200 > int(x) >= 18]
    child_ages_list = [int(x) for x in input_list if 0 < int(x) < 18]
    if len(adult_ages_list) != 0:
        avg_adult = sum(adult_ages_list) / len(adult_ages_list)
    else:
        avg_adult = "No adults on list"
    num_child = len(child_ages_list)

    return avg_adult, num_child


if __name__ == '__main__':
    peoples_ages = ['2', '8', '3', '18', '75', '21', '67', '16', '53', '23', '76', '1', '3', '45', '2', '67', '34']

    print('The average age of adults is: %s.' % (age_calculator(peoples_ages)[0]))
    print('There are %s children on this list.' % (age_calculator(peoples_ages)[1]))
