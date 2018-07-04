N = int(input())
files = dict()
for i in range(N):
    inp = input().split(" ")
    filename = inp[0]
    rights = inp[1:]
    files.setdefault(filename, rights)

M = int(input())
for i in range(M):
    access, filename = input().split(" ")
    rights = files.get(filename)

    if access == 'read' and 'R' in rights:
        print('OK')
    elif access == 'write' and 'W' in rights:
        print('OK')
    elif access == 'execute' and 'X' in rights:
        print('OK')
    else:
        print('Access denied')
