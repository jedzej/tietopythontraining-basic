OPERATION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}


def check_disk():
    file_permissions = {}
    for i in range(int(input())):
        file, *permissions = input().split()
        file_permissions[file] = set(permissions)

    for i in range(int(input())):
        operation, file = input().split()
        if OPERATION_PERMISSION[operation] in file_permissions[file]:
            print('OK')
        else:
            print('Access denied')


def main():
    check_disk()


if __name__ == '__main__':
    main()
