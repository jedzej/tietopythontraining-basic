def main():
    operations_dict = {
        'read': 'R',
        'write': 'W',
        'execute': 'X',
    }

    file_permissions = {}
    for x in range(int(input())):
        file, *operations = input().split()
        file_permissions[file] = set(operations)

    for x in range(int(input())):
        permiss, file = input().split()
        if operations_dict[permiss] not in file_permissions[file]:
            print("Access denied")
        else:
            print("OK")


if __name__ == '__main__':
    main()
