typeOfOperations = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}

filePermissions = {}

for i in range(int(input("How many files? "))):
    file, *permissions = input("Type the file name and permission").split()
    filePermissions[file] = set(permissions)

for x in range(int(input("How many files to check? "))):
    operation, file = input("Type the operation and name of the file ").split()
    if typeOfOperations[operation] in filePermissions[file]:
        print('OK')
    else:
        print('Access denied')
