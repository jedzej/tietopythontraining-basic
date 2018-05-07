# function return length for the longest string
def find_max_sting(my_dict):
    max_table = len(max(sum(my_dict, []), key=len))
    return max_table


# function print table with elements just to right
def print_table(my_dict, maximum):
    for row in my_dict:
        print(' '.join([elem.rjust(maximum) for elem in row]))


# function open file and set to list
def file_to_list(file_name):
    my_file = open(file_name, "r")
    words_list = my_file.read().split()
    return words_list
