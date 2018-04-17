"""
Age calculator - write a program that for given list
of people's ages calculate the average age of adults
(age >= 18) and count the children (age < 18).
Use list comprehensions.
"""


def input_list():
    print("Please input ages of people; input -1 to stop")
    ages = []
    while True:
        age = int(input())
        if age == -1:
            break
        ages.append(age)

    return ages


def main():
    ages = input_list()
    adults = [x for x in ages if x > 18]

    if len(adults) > 0:
        print("Average of adults age = " +  str(sum(adults) / len(adults)))
    print("Number of children = " + str(len(ages) - len(adults)))


if __name__ == '__main__':
    main()
