#!/usr/bin/env python3


OPERATIONS = {'write': 'W', 'read': 'R', 'execute': 'X'}
access_rights_database = {}


def check_access_right(operation, file):
    operation_on_file = OPERATIONS.get(operation)
    file_access_rights = access_rights_database.get(file)

    if operation_on_file and file_access_rights:
        if operation_on_file in file_access_rights:
            return "OK"
        else:
            return "Access denied"
    else:
        return "There is no such file/operation in database"


def get_input_number_of(item_name):
    try:
        number = int(input("Please enter number of {}\n".format(item_name)))
    except ValueError:
        print("Wrong number, try again\n")
        exit()
    return number


def get_input_list_of(input_prompt):
    output_list = input(input_prompt).split()
    if len(output_list) < 2:
        print("Not enough arguments, check your input\n")
        exit()
    return output_list


def main():
    for _ in range(get_input_number_of("files")):
        file_perms_list = get_input_list_of(
            "Enter name of file and it's permission seperated with spaces"
            " [file R W X]\n")
        file_name = file_perms_list[0]
        perms_list = file_perms_list[1:]
        access_rights_database.update({file_name: perms_list})

    for _ in range(get_input_number_of("operations")):
        operation, file = get_input_list_of(
            "Enter: [write/read/execute] [filename]\n")
        print(check_access_right(operation, file))


if __name__ == "__main__":
    main()
