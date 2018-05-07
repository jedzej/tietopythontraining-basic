#!/usr/bin/env python3


def age_calculator(list_of_ages):
    children_ages = [x for x in list_of_ages if x < 18 and x > 0]
    adults_ages = [x for x in list_of_ages if x >= 18]
    if len(adults_ages) > 0:
        return sum(adults_ages) / len(adults_ages), len(children_ages)
    else:
        return 0, len(children_ages)


def main():
    try:
        in_list_of_ages = [float(i) for i in input(
            "Please enter age numbers separated with spaces\n").split()]
    except ValueError:
        print("Something went wrong with your input, please try again")
        exit()

    print("Average adult age is: {} and there were {} children in the list"
          .format(*age_calculator(in_list_of_ages)))


if __name__ == "__main__":
    main()
