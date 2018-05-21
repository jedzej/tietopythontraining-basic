# function return length for the longest strings in array
def find_max_sting(my_dict):
    # sum set all strings from array to list, next search
    # longest word(max), and return strings length
    max_table = len(max(sum(my_dict, []), key=len))
    return max_table


# function return length for the longest string in array
def find_max_sting2(my_dict):
    max_str = len(my_dict[0][0])
    for row in my_dict:
        max_row = len(max(row, key=len))
        print(max_row, max_str)
        if max_row > max_str:
            max_str = max_row
    return max_str


# function print table with elements just to right
def print_table(my_dict, maximum):
    for row in my_dict:
        print(' '.join([elem.rjust(maximum) for elem in row]))


# function open file and set to list
def file_to_list(file_name):
    my_file = open(file_name, "r")
    words_list = my_file.read().split()
    return words_list
