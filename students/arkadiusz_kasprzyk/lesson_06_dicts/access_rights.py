# access_right.py

symbols = {'execute': 'X', 'read': 'R', 'write': 'W'}

N = int(input("Give N: "))
file_rights = dict()

for k in range(N):
    filename, *rights = input("{}: ".format(k + 1)).split()
    file_rights[filename] = set(rights)
    """ or
    file_k = input("{}: ".format(k + 1)).split(" ")
    rights[file_k[0]] = set(file_k[1:])
    """

M = int(input("Give M: "))
commands = [''] * M

for k in range(M):
    commands[k] = input("{}: ".format(k + 1)).split()
    # e.g. "execute file.ext" -- always 2 words!

print("")  # just aesthetics for testing in Snakify

for k in range(M):
    """ in one line
    if symbols[commands[k][0]] in rights[commands[k][1]]:
    """
    command, filename = commands[k]
    if symbols[command] in file_rights[filename]:
        print("OK")
    else:
        print("Access denied!")
