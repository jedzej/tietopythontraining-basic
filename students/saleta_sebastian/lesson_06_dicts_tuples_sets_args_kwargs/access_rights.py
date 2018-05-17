OPERATION_PERMISSION = {
    'read' : 'R',
    'write' : 'W',
    'execute' : 'X'
}


files_with_access_rigts = {}


def check_access(operation, file_name):
    if operation in OPERATION_PERMISSION.keys():
        if(file_name in files_with_access_rigts.keys()):

            if(OPERATION_PERMISSION[operation]
                    in files_with_access_rigts[file_name]):
                print('OK')
            else:
                print('Access denied')
        else:
            print('File not exist in db')
    else:
        print("Wrong operation")


def main():
    files = 0
    try:
        files = (int(input('How many files you want add? ')))
    except ValueError:
        print("Something wrong try again")
        print("Something wrong try again")

    for i in range(files):
        list_of_files = \
            input("input file and access rights seperate by spaces: ").split()
        if len(list_of_files) >= 2:
            file_name = list_of_files[0]
            file_access_rihts = list_of_files[1:]
            files_with_access_rigts.update({file_name : file_access_rihts})
        else:
            print('probably you dont give access rights')
    operations = 0
    try:
        operations = int(input('How many operations you wanna make? '))
    except ValueError:
        print("Something wrong try again")

    for k in range(operations):
        operation, file_name = \
            input("enter operation and file name separeted by space").split()
        check_access(operation, file_name)


if __name__ == '__main__':
    main()
