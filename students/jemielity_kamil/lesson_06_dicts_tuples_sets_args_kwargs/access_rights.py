
Dictionary = {}
Perms = {'read': 'R', 'write': 'W', 'execute': 'X'}
for i in range(int(input('Number of files: '))):
    file_name, *permissions = (input("File name and permissions: ")).split()
    Dictionary[file_name] = permissions

for j in range(int(input('How many actions on files: '))):
    action, file = (input("Action and file: ")).split()
    if Perms[action] in Dictionary[file]:
        print('OK')
    else:
        print('Access denied')
