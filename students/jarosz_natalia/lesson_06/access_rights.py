def access_rights():
    operation_permission = {'read': 'R',
                            'write': 'W',
                            'execute': 'X'}

    file_permissions = {}
    for i in range(int(input())):
        file, *permissions = input().split()
        file_permissions[file] = set(permissions)

    for i in range(int(input())):
        operation, file = input().split()
        if operation_permission[operation] in file_permissions[file]:
            print('OK')
        else:
            print('Access denied')


def main():
    access_rights()


if __name__ == '__main__':
    main()
