# You need to recover the control over the access rights to the files. For
# each request your program should return OK if the requested operation is
# valid or Access denied if the operation is invalid.


def check_rights(command, rights):

    if command == 'read':
        symbol = 'R'
    elif command == 'write':
        symbol = 'W'
    elif command == 'execute':
        symbol = 'X'

    if symbol in rights:
        return "OK"
    else:
        return "Access denied."


def main():
    files = dict()
    results = dict()
    file_number = int(input("Enter number of files: "))

    for i in range(file_number):
        file_name, file_rights = input().split(' ', 1)
        files[file_name] = file_rights

    command_number = int(input("Enter command number: "))

    for i in range(command_number):
        command, used_file = input().split()
        results[i] = check_rights(command, files[used_file])

    for v in results.values():
        print(v)


if __name__ == '__main__':
    main()
