'''
Age calculator - write a program that for given list of people's
ages calculate the average age of adults (age >= 18) and count
the children (age < 18). Use list comprehensions.
'''


def calculate_age(ages):
    children = 0
    sum = 0
    for i in range(len(ages)):
        if (ages[i] < 18):
            children += 1
        else:
            sum += ages[i]
    print("Average age of adults is: ", sum /
          (len(ages) - children), ", count of children:", children)


if __name__ == "__main__":
    try:
        ages = [int(s) for s in input(
            "Enter list of ages separated by space: ").split()]
        calculate_age(ages)
    except ValueError:
        print("Invalid input.")
