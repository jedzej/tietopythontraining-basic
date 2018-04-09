
def is_adult(x):
    return x >= 18


def main():
    people_ages_list = [int(i) for i in input().split()]
    adults_ages_list = [i for i in people_ages_list if is_adult(i)]
    children_ages_list = [i for i in people_ages_list if not is_adult(i)]
    # Another way to get children ages:
    # children_ages_list = [i for i in people_ages_list if i not in adults_ages_list]

    avg_age_of_adults = sum(adults_ages_list) / len(adults_ages_list)
    count_children = len(children_ages_list)
    print("Average age of adults: %f" % avg_age_of_adults)
    print("Number of children: %d" % count_children)


if __name__ == "__main__":
    main()
