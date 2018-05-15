access_rights = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
    }

files = {}
for _ in range(int(input())):
    file_access = input().split()
    files[file_access[0]] = ''.join(file_access[1:])

for _ in range(int(input())):
    operation, file = input().split()
    if access_rights[operation] in files[file]:
        print('OK')
    else:
        print('Access denied')
