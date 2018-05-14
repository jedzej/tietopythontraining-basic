def age_calculator(people_age_list):
    adults = [int(k) for k in people_age_list if k >= 18]
    children = [int(c) for c in people_age_list if c < 18]
    average_children = 0
    average_adults = 0

    if len(adults) > 0:
        average_adults = sum(adults) / len(adults)
    if len(children) > 0:
        average_children = sum(children) / len(children)

    print('Average adult age is: {} and average children age is {}'
        .format(average_adults, average_children))




def main():
    list_of_ages = [int(i) for i in input().split()]
    age_calculator(list_of_ages)


if __name__ == '__main__':
    main()
