possible_permissions = {'read': 'R', 'write': 'W', 'execute': 'X', }

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    operation, file = input().split()
    if possible_permissions[operation] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')
