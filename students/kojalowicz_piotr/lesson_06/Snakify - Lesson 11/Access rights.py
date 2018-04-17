permissions_for_file = {}
Perms = {'read': 'R', 'write': 'W', 'execute': 'X'}

for i in range(int(input())):
    file_name, *permissions = (input()).split()
    permissions_for_file[file_name] = permissions

for j in range(int(input())):
    action, file = (input()).split()
    if Perms[action] in permissions_for_file[file]:
        print('OK')
    else:
        print('Access denied')
