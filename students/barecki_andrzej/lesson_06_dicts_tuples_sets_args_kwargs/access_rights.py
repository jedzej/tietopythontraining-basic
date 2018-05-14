def main():
    """"Create empty dictionary of files"""
    dict_files = dict()

    """"set number of files in dictionary"""
    number_of_files_in_dict = int(input())

    """"Add files to dictionary"""
    for _ in range(number_of_files_in_dict):
        single_file = [x for x in input().split(' ')]
        dict_files[single_file[0]] = set(single_file[1:])

    """"set number of files that will be checked"""
    number_of_files_to_check = int(input())

    """"check access rights based on dictionary"""
    for _ in range(number_of_files_to_check):
        operation, file = [x for x in input().split(" ")]

        """"convert string for related operation"""
        if operation == "write":
            operation = "W"
        elif operation == "read":
            operation = "R"
        elif operation == "execute":
            operation = "X"
        else:
            print("improper set of operation")

        if operation in dict_files[file]:
            print("OK")
        else:
            print("Access denied")


if __name__ == '__main__':
    main()
