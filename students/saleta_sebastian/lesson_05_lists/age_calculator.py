def age_calculator(list):
    adults = [int(k) for k in list if k >= 18]
    children = [int(c) for c in list if c < 18]

    if len(adults) > 0:
        average_adults = sum(adults) / len(adults)
    if len(children) > 0:
        average_children = sum(children) / len(children)

    print(average_adults)
    print(average_children)


def main():
    list_of_ages = [int(i) for i in input().split()]
    age_calculator(list_of_ages)


if __name__ == '__main__':
    main()
