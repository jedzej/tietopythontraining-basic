
permissions = {'read': 'R', 'write': 'W', 'execute': 'X'}


def recover_control():

    file_permissions = {}

    for i in range(int(input())):
        file, *current_permissions = input().split()
        file_permissions[file] = set(current_permissions)

    for i in range(int(input())):
        operation, file = input().split()
        if permissions[operation] in file_permissions[file]:
            print('OK')
        else:
            print('Access denied')


if __name__ == '__main__':
    recover_control()
