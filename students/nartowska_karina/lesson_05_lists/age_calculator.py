def average_age(values):
    average = 0
    adult = 0
    for i in values:
        if i >= 18:
            average += i
            adult += 1
    if adult > 0:
        print("The average age of adults: ")
        return average / adult
    else:
        print("The average age of adults: ")
        return 0


def count_the_children(values):
    children = 0
    for i in values:
        if i < 18:
            children += 1
    print("Count the children: ")
    return children


def data():
    input_value = input().split()
    output_value = []
    for j in input_value:
        output_value.append(int(j))
    return output_value


def main():
    print("Enter data:")
    values = data()
    print(average_age(values))
    print(count_the_children(values))


if __name__ == "__main__":
    main()
