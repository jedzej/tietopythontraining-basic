def read_rights(num):
    files = dict()
    for _ in range(num):
        file_name, *allowed_operations = input().split()
        files[file_name] = allowed_operations
    return files


def check_rights(num, files):
    rights = {'write': 'W', 'read': 'R', 'execute': 'X'}
    for _ in range(num):
        operation, file = input().split()
        if rights.get(operation) in files.get(file):
            print('OK')
        else:
            print('Access denied')


num_of_files = int(input('Give the number of files: '))
print('Input files with rights:')
files_with_rights = read_rights(num_of_files)
num_of_operations = int(input('Give the number of operations: '))
print('Input operations with file name:')
check_rights(num_of_operations, files_with_rights)
