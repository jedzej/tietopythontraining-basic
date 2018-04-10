def calculate_average_age(list_of_ages):
    adult_numbers = 0
    adult_age_summary = 0
    child_numbers = 0
    for element in list_of_ages:
        if element >= 18:
            adult_age_summary += element
            adult_numbers += 1
        else:
            child_numbers += 1
    return adult_age_summary / adult_numbers, child_numbers


def main():
    list_of_ages = [10, 8, 23, 56, 78, 6, 4, 35]
    print("Average ages for adults %f, number of children %d" % calculate_average_age(list_of_ages))


if __name__ == "__main__":
    main()
