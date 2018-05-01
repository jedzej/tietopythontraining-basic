def read_permissions_set():
    input_array = input().split()
    key = input_array[0]

    permissions = set()
    for i in input_array[1:]:
        permissions.add(i.lower())

    return (key, permissions)


def read_files():
    number_of_files = int(input('Enter number of files: '))

    files = dict()
    for i in range(number_of_files):
        permissions = read_permissions_set()
        files[permissions[0]] = permissions[1]

    return files


def read_operations():
    number_of_operations = int(input('Enter number of operations: '))
    operations = []
    for i in range(number_of_operations):
        input_array = input().split()
        operations += [{'file_name': input_array[1],
                        'action': input_array[0]}]

    return operations


def get_required_permission(operation):
    if operation == 'read':
        return 'r'
    if operation == 'write':
        return 'w'
    if operation == 'execute':
        return 'x'
    raise(ValueError)


def perform_operation(permissions, operation):
    if get_required_permission(operation) in permissions:
        print('OK')
    else:
        print('Access denied')


if __name__ == '__main__':
    files = read_files()
    operations = read_operations()

    print(end='\n')
    for operation in operations:
        permissions = files[operation['file_name']]
        perform_operation(permissions, operation['action'])
