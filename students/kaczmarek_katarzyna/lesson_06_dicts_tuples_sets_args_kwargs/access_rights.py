OPERATION_PERMISSION = dict(read='R', write='W', execute='X')


def main():
    file_permissions = {}
    for i in range(int(input("The number of files "
                             "contained in the filesystem: "))):
        file, *permissions = input("#" + str(i + 1) + " Type file name and "
                                   "allowed operations "
                                   "(ex. fileName.txt R W): ").split()
        file_permissions[file] = set(permissions)

    for i in range(int(input("The number of operations to the files: "))):
        operation, file = input("Specify the operation that "
                                "is requested for file (ex. write "
                                "fileName.txt) #" + str(i + 1) + ":").split()
        if OPERATION_PERMISSION[operation] in file_permissions[file]:
            print('OK')
        else:
            print('Access denied')


if __name__ == '__main__':
    main()
