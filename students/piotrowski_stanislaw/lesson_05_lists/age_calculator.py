# piotrsta
# Age calculator
# Write a program that for given list of people's ages
# calculate the average age of adults (age >= 18)
# and count the children (age < 18). Use list comprehensions.


def average_age(input_list):
    adult_ages_list = [int(x) for x in input_list if int(x) >= 18]
    child_ages_list = [int(x) for x in input_list if int(x) < 18]
    avg_adult = sum(adult_ages_list) / len(adult_ages_list)
    avg_child = sum(child_ages_list) / len(child_ages_list)

    return avg_adult, avg_child


if __name__ == '__main__':
    peoples_ages = ['2', '8', '3', '18', '75', '21', '67', '16', '53', '23', '76', '1', '3', '45', '2', '67', '34']

    print('The average age of adults is: %s.' % (average_age(peoples_ages)[0]))
    print('The average age of children is: %s.' % (average_age(peoples_ages)[1]))
