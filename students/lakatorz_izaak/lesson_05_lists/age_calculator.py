# Numbers filter - using list comprehensions write a function that casts
# list of strings to list of integers and filters numbers within supplied
# range. Example data:


def average_age(user_list):
    list_of_age = [int(value) for value in user_list]

    adult_list = [age for age in list_of_age if age >= 18]
    child_list = [age for age in list_of_age if age < 18]

    average_adults = sum(adult_list)/len(adult_list)
    average_children = sum(child_list)/len(child_list)

    return average_adults, average_children


def main():
    list_of_strings = ['2', '38', '53', '11', '31', '52', '16', '7', '69']

    av_adults, av_children = average_age(list_of_strings)

    print("Average age for adults is equal to " + str(round(av_adults)))
    print("Average age for children is equal to " + str(round(av_children)))


if __name__ == "__main__":
    main()
