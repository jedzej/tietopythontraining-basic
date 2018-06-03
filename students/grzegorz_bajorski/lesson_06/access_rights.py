def check_access(rights):
    if rights == 'read':
        return 'R'
    if rights == 'write':
        return 'W'
    if rights == 'execute':
        return 'X'


n = int(input())
files = {}

for _ in range(n):
    names, *access = input().split()
    files[names] = set(access)

m = int(input())
for _ in range(m):
    method, file_name = input().split()
    for names, access in files.items():
        if file_name in names:
            if check_access(method) in access:
                print('OK')
            else:
                print('Access denied')
