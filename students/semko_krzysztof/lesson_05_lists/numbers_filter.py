"""
Numbers filter - using list comprehensions write
a function that casts list of strings to list of
integers and filters numbers within supplied range.
Example data:

list_of_strings = ['2', '0', '8', '3']
to_filter_range = range(3)
expected_output = [8, 3]

"""


def in_range(num, range_number):
    range_list = range(range_number)
    if num in range_list:
        return True
    return False


def main():
    print("Please input one char numbers to filter:")
    list_of_strings = input().split()
    print("Please input range to filter list:")
    range_number = int(input())

    ranged_list = [int(num) for num in list_of_strings
                   if in_range(int(num), range_number)]

    print(' '.join(str(i) for i in ranged_list))


if __name__ == '__main__':
    main()
