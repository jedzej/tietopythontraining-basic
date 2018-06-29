def average_age(list_of_people):
    adult_numbers = 0
    adult_age_summary = 0
    child_numbers = 0

    for el in list_of_people:
        if int(el) >= 18:
            adult_age_summary += int(el)
            adult_numbers += 1
        else:
            child_numbers += 1

    if adult_age_summary == 0:
        return adult_age_summary, child_numbers
    return adult_age_summary / adult_numbers, child_numbers


def main():
    list_of_people = ['2', '0', '58', '38']
    print("Average ages for adults %f, number of children %d"
          % average_age(list_of_people))


if __name__ == "__main__":
    main()
