# Statement
# A sequence consists of integer numbers and ends with the number 0.
# Determine how many elements of this sequence are equal to its
# largest element.


def count_max_elements():
    print("Enter integer number (0 to end processing):")
    maximum = int(input())
    a = maximum
    max_count = 1
    while(a != 0):
        print("Enter integer number (0 to end processing):")
        a = int(input())
        if (a > maximum):
            maximum = a
            max_count = 1
        elif (a == maximum):
            max_count += 1
    print("The count of elements of this sequence that "
          "are equal to its largest element is:")
    print(max_count)


if __name__ == '__main__':
    count_max_elements()
