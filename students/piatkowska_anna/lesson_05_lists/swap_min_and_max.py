'''
Given a list of unique numbers, swap the minimal and maximal
elements of this list. Print the resulting list.
'''


def swap_min_max():
    a = input("Enter list of numbers separated by space: ").split()
    for i in range(len(a)):
        a[i] = int(a[i])
    minimal_index = 0
    maximal_index = 0

    for i in range(len(a)):
        if (a[i] > a[maximal_index]):
            maximal_index = i
        if a[i] < a[minimal_index]:
            minimal_index = i
    a[minimal_index], a[maximal_index] = a[maximal_index], a[minimal_index]
    print(' '.join([str(i) for i in a]))


if __name__ == "__main__":
    try:
        swap_min_max()
    except ValueError:
        print("Invalid input, it should be numbers separated by space.")
