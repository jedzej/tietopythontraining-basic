def main():
    adult_age = 18
    list_of_ages = [int(x) for x in input().split()]
    children = [x for x in list_of_ages if x < adult_age]
    adults = [x for x in list_of_ages if x >= adult_age]
    number_of_children = len(children)
    average_adult_age = sum(adults) / len(adults)
    print("Number of children {0}, avarage adult age {1}"
          .format(number_of_children, round(average_adult_age, 2)))


if __name__ == '__main__':
    main()
