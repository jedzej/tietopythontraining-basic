'''
Given a list of numbers, determine and print the quantity of elements that are
greater than both of their neighbors.
The first and the last items of the list shouldn't be considered because they
don't have two neighbors.
'''


def greater_than_neighbours():
    a = input("Enter list of numbers separated by space: ").split()
    for i in range(len(a)):
        a[i] = int(a[i])
    count = 0
    for i in range(1, len(a) - 1):
        if a[i] > a[i + 1] and a[i] > a[i - 1]:
            count += 1
    print("There is " + str(count) +
          " elements that are greater then its neighbours.")


if __name__ == "__main__":
    try:
        greater_than_neighbours()
    except ValueError:
        print("Invalid list of numbers")
