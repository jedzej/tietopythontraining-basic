files_nr = int(input())
files = {}
for i in range(files_nr):
    line_str = input()
    line_list = line_str.split(' ')
    acces_right_list = []

    for acces_right in line_list[1:]:
        acces_right_list.append(acces_right)
    files.setdefault(line_list[0], acces_right_list)

files_nr = int(input())
for i in range(files_nr):
    line_str = input()
    line_list = line_str.split(' ')
    acces_right_list = files[line_list[1]]
    access = 0
    for acces_right in acces_right_list:
        if acces_right == 'R' and line_list[0] == 'read':
            access = 1
            break
        elif acces_right == 'W' and line_list[0] == 'write':
            access = 1
            break
        elif acces_right == 'X' and line_list[0] == 'execute':
            access = 1
            break
    if access == 1:
        print('OK')
    else:
        print('Access denied')
