# Write a program that for given list of people's ages calculate
# the average age of adults (age >= 18) and count the children
# (age < 18). Use list comprehensions.


def main():
    age_list = []
    number_of_children = 0
    average_adult_age = 0

    print("Enter the mount of people:")
    N = int(input())
    print("Enter people's ages (one by one):")
    for x in range(N):
        x = int(input())
        age_list.append(x)

    adults = [x for x in age_list if x >= 18]
    children = [x for x in age_list if int(x) < 18]
    average_adult_age = sum(adults) / len(adults)
    number_of_children = len(children)

    print("Average adult age: %.2f" % average_adult_age)
    print("Number of children: %d" % number_of_children)


if __name__ == "__main__":
    main()
